<!DOCTYPE html>
<html>
	<head>
		<title>Bee Movie Game</title>
	</head>
	<body>
		<h1>Bee Movie Game</h1>
           <img src="http://www.websignia.net/wp-content/uploads/2014/04/ws_reloaded_portfolio_beemovie_header_bee.png" height="200px" />
		<h2>Instructions</h2>
           <p>One word is missing from the Bee Movie Script.  Pick the 
              correct replacement.</p>
           <h3>{{scramble_dict['display']}}</h3>
          <form action="/check/missing/{{scramble_dict["missing_word"]}}/line/{{scramble_dict['line_number']}}/streak/{{streak}}" method="POST">
          % for index, choice in enumerate(scramble_dict['choices']):
                <button name="answer" value={{choice}}>{{choice}}</button>
          % end
          </form>
          <h3>Streak: {{streak}}</h3>
	</body>
</html>
