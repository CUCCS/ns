@load protocols/ssh/detect-bruteforcing

redef SSH::password_guesses_limit=10;

hook Notice::policy(n: Notice::Info)
	{
	if ( n$note == SSH::Password_Guessing )
		add n$actions[Notice::ACTION_EMAIL];
	}

