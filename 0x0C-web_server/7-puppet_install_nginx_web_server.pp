# Install Nginx web server (w/ Puppet)

# Define a class for the Nginx configuration
class nginx_config {
    package { 'nginx':
        ensure => 'installed',
    }

    file { '/var/www/html/index.html':
        content => 'Hello World!',
        require => Package['nginx'],
    }

    service { 'nginx':
        ensure => 'running',
        enable => true,
        require => Package['nginx'],
    }
}

# Define a class for the redirection configuration
class redirect_config {
    file { '/etc/nginx/sites-available/redirect':
        ensure => 'present',
        content => "server {
            listen 80;
            server_name _;
            location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
            }
        }",
        require => Class['nginx_config'],
    }

    file { '/etc/nginx/sites-enabled/redirect':
        ensure => 'link',
        target => '/etc/nginx/sites-available/redirect',
        require => File['/etc/nginx/sites-available/redirect'],
    }

    exec { 'nginx_reload':
        command => 'service nginx reload',
        refreshonly => true,
        subscribe => [File['/etc/nginx/sites-available/redirect'], File['/etc/nginx/sites-enabled/redirect']],
    }
}

# Apply both classes
include nginx_config
include redirect_config
