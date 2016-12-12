<!DOCTYPE html>
<html>
	<head>
		<title>Bee Movie Game</title>
	</head>
	<body>
		<h1>Bee Movie Game</h1>
		<h2>Instructions</h2>
           <p>One word is missing from the Bee Movie Script.  Pick the 
              correct replacement.</p>
           <h3>{{scramble_dict['display']}}</h3>
          <form action="/check/missing/{{scramble_dict["missing_word"]}}" method="POST">
          % for index, choice in enumerate(scramble_dict['choices']):
                <button name="answer" value={{choice}}>{{choice}}</button>
          % end
          </form>
          {{scramble_dict}}
	</body>
</html>
