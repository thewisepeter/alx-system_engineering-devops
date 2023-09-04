# Define a class for Nginx configuration
class nginx_redirect {
    package { 'nginx':
        ensure => 'installed',
    }

    service { 'nginx':
        ensure => 'running',
        enable => true,
    }

    file { '/var/www/html/index.html':
        ensure  => 'file',
        content => 'Hello World!',
    }

    file { '/var/www/html/404.html':
        ensure  => 'file',
        content => "Ceci n'est pas une page",
    }

    file { '/etc/nginx/sites-available/default':
        ensure  => 'file',
        content => template('nginx/default.erb'),
        notify  => Service['nginx'],
    }

    file { '/etc/nginx/sites-enabled/default':
        ensure => 'link',
        target => '/etc/nginx/sites-available/default',
    }
}

# Apply the Nginx configuration class
include nginx_redirect

