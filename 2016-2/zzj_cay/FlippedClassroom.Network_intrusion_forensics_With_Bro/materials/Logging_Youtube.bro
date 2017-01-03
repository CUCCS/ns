module YouTube;

export {
    # The fully resolve name for this will be YouTube::LOG    
    redef enum Log::ID += { LOG };

    type Info: record {
        ts:    time    &log;
        uid:   string  &log;
        id:    conn_id &log;
        host:  string  &log;
        uri:   string  &log;
        title: string  &log;
        };
}

global title_set: set[string];

event bro_init() &priority=5
    {
    Log::create_stream(YouTube::LOG, [$columns=Info]);
    }

event http_reply(c: connection, version: string, code: count, reason: string)
    {
    if ( c$http$method == "GET" && /\.youtube\.com$/ in c$http$host && /^\/watch\?v=/ in c$http$uri )
        {
        add title_set[c$uid];
        }
    }

event http_entity_data(c: connection, is_orig: bool, length: count, data: string)
    {
    if ( is_orig )
        {
        return;
        }

    if ( c$uid in title_set )
        {
        if ( /\<title\>/ in data && /\<\/title\>/ in data )
            {
            local temp: table[count] of string;
            temp = split(data, /\<\/?title\>/);
            if ( 2 in temp )
                {
                local log_rec: YouTube::Info = [$ts=network_time(), $uid=c$uid, $id=c$id, $host=c$http$host, $uri=c$http$uri, $title=temp[2]];
                Log::write(YouTube::LOG, log_rec);
                delete title_set[c$uid];
                }
            }
        }
    }
