# [Self Introduction Chatbot by Yu Hsuan Chen](https://github.com/iitsmel/bot)


## Platfrom
- front-end : 
  - LINE Login for LIFF by Vue.js and Ngrok
- back-end : 
  - Heroku for Chatbot
- additional:
  - unit test for front-end 

## Problems I've Encountered & Currently Solved
- unit test
  - At first, I transfered all incomming message to english. But when I performed unit test, it seems like it'll detect "Non-ASCII character". So I detect whether the incomming message is English words or not. If is English words, then transfer to lower case. ( import enchant )
- Heroku h10 error
  - Solution: Use the Internet. I've encountered different h10 issues and sometimes the solution is diferent. Search something like "Heroku h10" or "Heroku line bot h10" with or without the word "error", both works. "h10" already indicated the error message.
- Any Heroku issues 
  - I'd suggest read the error messages in log. It's difficult to  isolate the error messages and other messages, but it's better with clear error message if one wants to fix the problem fast. 
- Ngrok can't successfuly start running
  - Simply enter the location you stored Ngrok

## Learning Resources 
[Vue.js](https://v3.vuejs.org/guide/mobile.html#introduction)
[invalid host header](https://stackoverflow.com/questions/45425721/invalid-host-header-when-ngrok-tries-to-connect-to-react-dev-server)
[vue icon problem](https://www.xspdf.com/resolution/50778850.html)
[python unit test](https://queirozf.com/entries/python-unittest-examples-mocking-and-patching)
[cypress for end to end test](https://docs.cypress.io/guides/getting-started/installing-cypress.html#Adding-npm-scripts)