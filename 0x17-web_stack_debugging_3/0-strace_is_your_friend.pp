# This is intended to fix a wordpress serevr error

exec {
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin '
}
