@load base/protocols/http/main


event connection_established(c: connection)
    {
            if ( (c$id$orig_h == 192.168.121.147 ||
                  c$id$orig_h == 192.168.121.157 ||
                  c$id$orig_h == 192.168.121.167 ||
                  c$id$orig_h == 192.168.121.177 ||
                  c$id$orig_h == 192.168.121.184) &&
                 c$id$resp_h == 85.47.63.142 )
                    {
                    c$extract_orig = T;
                    c$extract_resp = T;
                    }
    }