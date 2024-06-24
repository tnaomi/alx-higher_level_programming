# Create a PP File
file { '/tmp/school':
  ensure  => file, # Make sure the file Exists
  path    => '/tmp/school', # PATH
  mode    => '0744',           # Permissions
  owner   => 'www-data',       # Owner
  group   => 'www-data',       # Group
  content => 'I love Puppet',  # Content
}
