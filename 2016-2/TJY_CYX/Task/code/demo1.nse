local shortport = require "shortport"
local http = require "http" 
local stdnse = require "stdnse" 
local string = require "string" 
 
-- The Rule Section -- 
portrule = shortport.http 
 
-- The Action Section -- 
action = function(host, port) 
 
    local uri = "/test.html" 
    local options = {header={}} 
    options['header']['User-Agent'] = "Mozilla/5.0 (compatible; demo1.nse)" 
	local response = http.get(host, port, uri, options) 
    if ( response.status == 200 ) then 
        local title = response.header['server']
        return title
    end 
end 
