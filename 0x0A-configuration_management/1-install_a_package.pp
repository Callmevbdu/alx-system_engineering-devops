# Puppet manifest for installing Flask version 2.1.0 using pip3
# Package name is Flask
# Version must be 2.1.0

# Ensure that python3-pip is installed before installing Flask
package {
  'python3-pip':
    ensure => installed,
}

# Install Flask using pip3
exec {
  'install_flask':
    command => '/usr/bin/pip3 install Flask==2.1.0',
    path    => '/usr/bin',
    unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}

# Ensure ownership and permissions for pip cache directory if necessary
file {
  '/root/.cache/pip':
    ensure => directory,
    owner  => 'root',
    group  => 'root',
    mode   => '0755',
}

