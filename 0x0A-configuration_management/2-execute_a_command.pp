# executes a command with pkill to kill killmenow process
exec { 'pkill':
command  => 'pkill -15 killmenow',
provider => 'shell',
}
