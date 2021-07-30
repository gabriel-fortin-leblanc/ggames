import ggames
import sys, os, io
import tempfile
import errno


PATH_TO_GRAPH_JSON = 'tests/tests_graph_json'


def test_create_parser():
    try:
        output = io.StringIO()
        sys.stdout = output
        temp_output = tempfile.NamedTemporaryFile('w+', delete=False)
        path_to_temp_output = os.path.join(tempfile.tempdir, temp_output.name)
        ggames.kcop_win(['1', os.path.join(PATH_TO_GRAPH_JSON, 'd_tree.json'),
                '--output', path_to_temp_output])
    except SystemExit as ex:
        assert ex.code == 0
        temp_output.seek(0)
        assert temp_output.readline() == 'True\n'
    else:
        assert False, 'The console scripts didn\'t exit.'
    finally:
        sys.stdout = sys.__stdout__
        if temp_output is not None:
            os.unlink(temp_output.name)

    try:
        output = io.StringIO()
        sys.stdout = output
        ggames.kcop_win(['1', os.path.join(PATH_TO_GRAPH_JSON, 'd_tree.json'),
                '--verbose'])
    except SystemExit as ex:
        assert ex.code == 0
        assert output.getvalue().split('\n') == [
                'Loading the graph...',
                'Graph loaded.',
                '"cop_robber_game.is_kcop_win" called.',
                '"cop_robber_game.get_game_graph" called.',
                '"cop_robber_game.game_graph_to_reachability_game" called.',
                '"reachability_game.get_attractor" called.',
                'True',
                '']
    finally:
        sys.stdout = sys.__stdout__

    try:
        output = io.StringIO()
        sys.stdout = output
        ggames.kcop_win(['--version'])
    except SystemExit as ex:
        assert ex.code == 0
        assert output.getvalue() == f'{ggames.PROGRAM_NAME} {ggames.VERSION}\n'
    else:
        assert False, 'The console scripts didn\'t exit.'
    finally:
        sys.stdout = sys.__stdout__


def test_extract_graph():
    with open(os.path.join(PATH_TO_GRAPH_JSON, 'd_tree.json')) as f:
        graph = ggames.extract_graph(f.read())
    assert len(graph) == 3
    V, E, tau = graph
    assert V == [1, 2, 3, 4, 5, 6, 7]
    assert E == [(1, 2), (2, 3), (3, 4), (2, 5), (5, 6), (3, 7)]
    assert tau == {(1, 2): '10', (2, 3): '01', (3, 4): '001', (2, 5): '010',
            (5, 6): '1', (3, 7): '001'}

    with open(os.path.join(PATH_TO_GRAPH_JSON, 'path4.json')) as f:
        graph = ggames.extract_graph(f.read())
    assert len(graph) == 2
    V, E = graph
    assert V == [1, 2, 3, 4, 5]
    assert E == [(1, 2), (2, 3), (3, 4), (4, 5)]


def test_error_extract_graph():
    try:
        output = io.StringIO()
        sys.stderr = output
        ggames.kcop_win(['1', os.path.join(PATH_TO_GRAPH_JSON,
                'error_unexpected_vertex_d_cycle5.json')])
    except SystemExit as error:
        assert error.code == errno.EINVAL
        assert output.getvalue() == 'Unexpected value detected in \'E\' '\
                'variable.'
    else:
        assert False, 'ValueError hadn\'t been thrown.'
    finally:
        sys.stderr = sys.__stderr__

    try:
        output = io.StringIO()
        sys.stderr = output
        ggames.kcop_win(['1', os.path.join(PATH_TO_GRAPH_JSON,
                'error_length_tau_d_cycle5.json')])
    except SystemExit as error:
        assert error.code == errno.EINVAL
        assert output.getvalue() == 'Unexpected number of elements in \'tau\''\
                ' variable.'
    else:
        assert False, 'ValueError hadn\'t been thrown.'
    finally:
        sys.stderr = sys.__stderr__

    try:
        output = io.StringIO()
        sys.stderr = output
        ggames.kcop_win(['1', os.path.join(PATH_TO_GRAPH_JSON,
                'error_unexpected_edge_pattern_d_cycle5.json')])
    except SystemExit as error:
        assert error.code == errno.EINVAL
        assert output.getvalue() == 'Unexpected value detected in \'tau\' '\
                'variable.'
    else:
        assert False, 'ValueError hadn\'t been thrown.'
    finally:
        sys.stderr = sys.__stderr__


def test_kcop_win():
    try:
        output = io.StringIO()
        sys.stdout = output
        ggames.kcop_win(['1', os.path.join(PATH_TO_GRAPH_JSON, 'path4.json')])
    except SystemExit as ex:
        assert ex.code == 0
        assert output.getvalue() == 'True\n'
    else:
        assert False, 'The console script didn\'t exit.'
    finally:
        sys.stdout = sys.__stdout__
    
    try:
        output = io.StringIO()
        sys.stdout = output
        ggames.kcop_win(['1', os.path.join(PATH_TO_GRAPH_JSON, 'cycle5.json')])
    except SystemExit as ex:
        assert ex.code == 0
        assert output.getvalue() == 'False\n'
    finally:
        sys.stdout = sys.__stdout__

    try:
        output = io.StringIO()
        sys.stdout = output
        ggames.kcop_win(['2', os.path.join(PATH_TO_GRAPH_JSON, 'cycle5.json')])
    except SystemExit as ex:
        assert ex.code == 0
        assert output.getvalue() == 'True\n'
    finally:
        sys.stdout = sys.__stdout__


def test_error_kcop_win():
    try:
        output = io.StringIO()
        sys.stderr = output
        ggames.kcop_win(['1', os.path.join(PATH_TO_GRAPH_JSON, 'cycle5.json'),
                '--output', 'a_wrong_path_to_the_json_dir/output'])
    except SystemExit as ex:
        assert ex.code == errno.ENOENT # No such file or directory
        assert output.getvalue() == 'The output file cannot be opened. '\
                'Check the permissions of the directory,\n'\
                'or if the file exists and cannot be overwritten.\n'\
                'No such file or directory'
    finally:
        sys.stderr = sys.__stderr__
    
    try:
        output = io.StringIO()
        sys.stderr = output
        ggames.kcop_win(['1', 'a_wrong_path_to_the_json_dir/graph.json'])
    except SystemExit as ex:
        assert ex.code == errno.ENOENT # No such file or directory
        assert output.getvalue() == 'The file containing the graph cannot be '\
                'opened. Check if the file exists\nand if the permission of '\
                'reading is granted.\n'\
                'No such file or directory'
    finally:
        sys.stderr = sys.__stderr__
    
    try:
        output = io.StringIO()
        sys.stderr = output
        ggames.kcop_win(['1', os.path.join(PATH_TO_GRAPH_JSON,
                'error_json_format_d_cycle5.json')])
    except SystemExit as ex:
        assert ex.code == errno.EINVAL
        assert output.getvalue() == 'The JSon is not well formatted.\n'\
                'Unterminated string starting at: line 3 column 5 (char 35)'
    finally:
        sys.stderr = sys.__stderr__
