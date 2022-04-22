from click.testing import CliRunner
from devilproject import devilproject

def test_hello_in_cli():
  runner = CliRunner()
  result = runner.invoke(devilproject, ['hello'], input='Hiago')
  assert 'Hellow World and hello Hiago' in result.output
  assert result.exit_code == 0