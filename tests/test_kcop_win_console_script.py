import ggames
import sys, os, io
import tempfile


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


def test_output_path():
    try:
        output = io.StringIO()
        sys.stdout = output
        temp_output = tempfile.NamedTemporaryFile('w+')
        path_to_temp_output = os.path.join(tempfile.tempdir, temp_output.name)
        ggames.kcop_win(['1', 'tests/graph_test_dir/d_tree.json',
                '--output', path_to_temp_output])
    except SystemExit as error:
        assert error.code == 0
        temp_output.seek(0)
        assert temp_output.readline() == 'True\n'
    else:
        assert False, 'The console scripts didn\'t exit.'
    finally:
        sys.stdout = sys.__stdout__
