# script that fixes Apache is returning a 500 error

$config_file = '/var/www/html/wp-settings.php'

exec { 'edit_file':
  command => "sed -i 's/phpp/php/g' ${config_file}",
  path    => ['/bin','/usr/bin']
}
