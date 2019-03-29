import twitter
from dateutil import parser
import matplotlib.pyplot as plt


user_id = "1108694717343166466"

api = twitter.Api(consumer_key='********************',
                  consumer_secret='********************',
                  access_token_key='********************',,
                  access_token_secret='********************',)

latest = api.GetUserTimeline(user_id, exclude_replies = True, trim_user = True, count = 1)

max_id = latest[0].id

results = {}
done = False

for i in range(0,5): ## HORROR!
        statuses = api.GetUserTimeline(user_id, exclude_replies = True, trim_user = True, max_id = max_id, count = 200)

        for s in statuses:
            if max_id > s.id: 
                    max_id = s.id

            if s.text.startswith('Automated Update: The Revoke Article 50 #petition has now hit'):
                try:    
                    count = int(s.text[62:71].replace(',', '').replace(' ', ''))
                    time = dt = parser.parse(s.created_at)

                    results[time] = count
                    print(str(time) + ' : ' + str(count))
                except ValueError:
                        pass


# Plot it
plt.plot(results.keys(), results.values())
plt.xlabel('Date')
plt.ylabel('Signatures')
plt.title('Revoke Article 50 petition count (from @BotRevoke)')
plt.show()