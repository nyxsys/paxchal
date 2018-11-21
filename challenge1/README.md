Sha encoder

TO RUN:
`npm i` then `node app.js`

super simple sha encoder microservice built on expressjs, lokijs, and nodejs


With regard to growth:
lokijs is the obvious first bottleneck as it isn't really meant to deal with large quantities of information and its in memory as opposed to on a seperate machine, meaning that every instance of this service will have an entirely different (and not particulraly scaleable) version of the database. This is an issue on a few levels:

-You're limited by the amount of space on the actual server as opposed to having storage somewhere else entirely (and likely far, far cheaper than upgrading how much in memory storage you have)
-I haven't put lokijs through loadtests but I can't imagine its meant for very many concurrent users, so race conditions are pretty much an immeadiate issue. 
-I'm sure you can create a permanent copy of the messages.json quite easily (though it'd still be on the server itself in this case), but as this project currently stands the entire database is reset every time the application restarts. 

The first and last can be solved by switching over to a dedicated service (in this case, to stick with noSQL, maybe mongodb might be an OK choice) the concurrency issue extends past the database choice and would require making sure that running several instances of this service across several different servers would not result in any write issues. Since any given hash is going to be effectively the same object in the database, overwrtting isn't really going to be that big of a worry. To some degree it'd be best if when user A submits a post and user B submits a get for the same new object it resolves user A then user B, but that might not be feasible on larger scales.