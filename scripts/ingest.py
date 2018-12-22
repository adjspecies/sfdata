import beautifulsoup4
import cookielib
import mechanize


br = mechanize.Browser()
jar = cookielib.LWPCookieJar()
br.set_cookiejar(jar)

br.set_handle_equiv( True ) 
br.set_handle_gzip( True ) 
br.set_handle_redirect( True ) 
br.set_handle_referer( True ) 
br.set_handle_robots( False ) 


