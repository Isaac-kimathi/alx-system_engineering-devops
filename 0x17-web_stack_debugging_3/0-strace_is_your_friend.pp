# Fix of wrong extension "phpp" to "php" in "wp-settings.php".

exec { 'replace_extension':
  command => "sed -i 's/phpp/php/g' '/var/www/html/wp-settings.php'",
  path    => ['/bin','/usr/bin']
}
