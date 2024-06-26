# Define an exec resource to increase open files limit
exec { 'increase_nginx_open_files' :
  environment => ['DIR=/etc/default/nginx',
                  'OLD=ULIMIT="-n 15"',
                  'NEW=ULIMIT="-n 15000"'],
  command     => 'sudo sed -i "s/$OLD/$NEW/" $DIR; sudo service nginx restart',
  path        => ['/usr/bin', '/bin'],
  returns     => [0, 1]
}
