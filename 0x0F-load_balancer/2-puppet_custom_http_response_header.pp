exec { 'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  path     => '/usr/bin',
  logoutput => true,
}

exec { 'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  path     => '/usr/bin',
  logoutput => true,
  require  => Exec['update'], # Ensure 'update' is executed first
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'), # Use a Puppet template
  require => Exec['install Nginx'], # Ensure 'install Nginx' is executed first
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
  path     => '/usr/bin',
  logoutput => true,
  require  => File['/etc/nginx/nginx.conf'], # Ensure the config file is in place
}
