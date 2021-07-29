from typing import final
import ggames
import sys, os, io
import tempfile


PATH_TO_GRAPH_JSON = 'tests/tests_graph_json'


def test_output_path():
    try:
        output = io.StringIO()
        sys.stdout = output
        temp_output = tempfile.NamedTemporaryFile('w+')
        path_to_temp_output = os.path.join(tempfile.tempdir, temp_output.name)
        ggames.kcop_win(['1', os.path.join(PATH_TO_GRAPH_JSON, 'd_tree.json'),
                '--output', path_to_temp_output])
    except SystemExit as error:
        assert error.code == 0
        temp_output.seek(0)
        assert temp_output.readline() == 'True\n'
    else:
        assert False, 'The console scripts didn\'t exit.'
    finally:
        sys.stdout = sys.__stdout__
        if temp_output is not None:
            temp_output.close()


def test_verbose():
    try:
        output = io.StringIO()
        sys.stdout = output
        ggames.kcop_win(['1', os.path.join(PATH_TO_GRAPH_JSON, 'd_tree.json'),
                '--verbose'])
    except SystemExit as error:
        assert error.code == 0
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


def test_version():
    try:
        output = io.StringIO()
        sys.stdout = output
        ggames.kcop_win(['--version'])
    except SystemExit as error:
        assert error.code == 0
        assert output.getvalue() == f'{ggames.PROGRAM_NAME} {ggames.VERSION}\n'
    else:
        assert False, 'The console scripts didn\'t exit.'
    finally:
        sys.stdout = sys.__stdout__


def test_error_extract_graph():
    try:
        output = io.StringIO()
        sys.stderr = output
        ggames.kcop_win(['1', os.path.join(PATH_TO_GRAPH_JSON,
                'error_unexpected_vertex_d_cycle5.json')])
    except SystemExit as error:
        assert error.code == 1
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
        assert error.code == 1
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
        assert error.code == 1
        assert output.getvalue() == 'Unexpected value detected in \'tau\' '\
                'variable.'
    else:
        assert False, 'ValueError hadn\'t been thrown.'
    finally:
        sys.stderr = sys.__stderr__
