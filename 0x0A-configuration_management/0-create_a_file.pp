file { 'school':
path => '/root/tmp/school',
mode => '0774',
group => 'www-data',
owner => 'www-data',
content => 'I love Puppet'
}
