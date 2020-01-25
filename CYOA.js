function option1()
{
	if(document.getElementById("button1").innerHTML=="Of course I'm ready! I'm always ready!")
	{
		document.getElementById("h1").innerHTML="Do you want to make a project?";
		document.getElementById("button1").innerHTML="YES Of course!";
		document.getElementById("button2").innerHTML="NO I don't";
		document.getElementById("image").src="start.jpg";
	}
	else if(document.getElementById("button1").innerHTML=="YES Of course!")
	{
		document.getElementById("h1").innerHTML="Great! choose your idea:";
		document.getElementById("button1").innerHTML="Make a project about CS";
		document.getElementById("button2").innerHTML="Make a project about making a project";
		document.getElementById("image").src="idea.jpeg";
	}
	else if(document.getElementById("button1").innerHTML=="Make a project about CS")
	{
		document.getElementById("h1").innerHTML="What will it be about?";
		document.getElementById("button1").innerHTML="Help the user learn CS";
		document.getElementById("button2").innerHTML="Give random facts about CS";
		document.getElementById("image").src="CS.jpg";
	}
	else if(document.getElementById("button1").innerHTML=="Help the user learn CS")
	{
		document.getElementById("h1").innerHTML="What language are you going to teach?";
		document.getElementById("button1").innerHTML="Python and Java Script";
		document.getElementById("button2").innerHTML="C and Assembly";
		document.getElementById("image").src="CS_languages.jpg";
	}
	else if(document.getElementById("button1").innerHTML=="Python and Java Script")
	{
		document.getElementById("h1").innerHTML="The user learned a lot from you and he is happy! Good job for you!! Thor sends a storm to show his appreciation!";
		document.getElementById("button1").innerHTML="RESTART";
		document.getElementById("button2").innerHTML="RESTART Please";
		document.getElementById("image").src="JS&Python.png";
	}
	else if(document.getElementById("button1").innerHTML=="About the invention of the computer")
	{
		document.getElementById("h1").innerHTML="The user now knows who invented the computer but he will definitely forget it by tomorrow so making this project was a waste of time. Instead you could have make global peace that will last forever but it's never too late to do it, start now";
		document.getElementById("button1").innerHTML="RESTART";
		document.getElementById("button2").innerHTML="RESTART Please";
		document.getElementById("image").src="make_peace.jpg";
	}
	else if(document.getElementById("button1").innerHTML=="Healthy food shop")
	{
		document.getElementById("h1").innerHTML="Well, except from Barak and a few others, no one bought from you because most people don't really search for healthy food shops, but don't be sad, Barak sends thanks";
		document.getElementById("button1").innerHTML="RESTART";
		document.getElementById("button2").innerHTML="RESTART Please";
		document.getElementById("image").src="thanks.gif";
	}
	else if(document.getElementById("button1").innerHTML=="Choose your own Adventure")
	{
		document.getElementById("h1").innerHTML="Do you want to do exactly what I did and make a project about making a project in which you can make a project about making a project?";
		document.getElementById("button1").innerHTML="YES, exactly!";
		document.getElementById("button2").innerHTML="NO, I want to make something else";
		document.getElementById("image").src="fair_use.jpg";
	}
	else if(document.getElementById("button1").innerHTML=="YES, exactly!")
	{
		document.getElementById("h1").innerHTML="NO! Do not do it! You should be creative and come up with your own idea! If Barak would see this, he would send a lightning right at you!";
		document.getElementById("button1").innerHTML="RESTART";
		document.getElementById("button2").innerHTML="RESTART Please";
		document.getElementById("image").src="NO.jpg";
	}
	else if(document.getElementById("button1").innerHTML=="RESTART")
	{
		document.getElementById("h1").innerHTML="You didn't say the magic word...";
		document.getElementById("button1").innerHTML="RESTART";
		document.getElementById("button2").innerHTML="RESTART Please";
		document.getElementById("image").src="magic.jpg";
		
	}
}

function option2()
{
	if(document.getElementById("button2").innerHTML=="I'm not ready but you don't really give me another choice")
	{
		document.getElementById("h1").innerHTML="Do you want to make a project?";
		document.getElementById("button1").innerHTML="YES Of course!";
		document.getElementById("button2").innerHTML="NO I don't";
		document.getElementById("image").src="start.jpg";
	}
	else if(document.getElementById("button2").innerHTML=="NO I don't")
	{
		document.getElementById("h1").innerHTML="Too bad! you don't have a project and you should be sad about it! Now run before mjolnir gets you! The Ragnarok has began!";
		document.getElementById("button1").innerHTML="RESTART";
		document.getElementById("button2").innerHTML="RESTART Please";
		document.getElementById("image").src="mjolnir.jpg";
	}
	else if(document.getElementById("button2").innerHTML=="Make a project about making a project")
	{
		document.getElementById("h1").innerHTML="What will your project be about?";
		document.getElementById("button1").innerHTML="Choose your own Adventure";
		document.getElementById("button2").innerHTML="Make a shop using HTML";
		document.getElementById("image").src="project.jpg";
	}
	else if(document.getElementById("button2").innerHTML=="Make a shop using HTML")
	{
		document.getElementById("h1").innerHTML="What kind of shop do you want it to be?";
		document.getElementById("button1").innerHTML="Healthy food shop";
		document.getElementById("button2").innerHTML="Fireball candy shop";
		document.getElementById("image").src="shop.png";
	}
	else if(document.getElementById("button2").innerHTML=="Fireball candy shop")
	{
		document.getElementById("h1").innerHTML="You made Ted happy! now he will have more fireballs for the MEET summer and everyone will be happy! Thanks to you, there will soon be global peace! Go tell Barak, he will be very happy to know";
		document.getElementById("button1").innerHTML="RESTART";
		document.getElementById("button2").innerHTML="RESTART Please";
		document.getElementById("image").src="peace.jpg";
	}
	else if(document.getElementById("button2").innerHTML==="Give random facts about CS")
	{
		document.getElementById("h1").innerHTML="What kind of facts are you going to give?";
		document.getElementById("button1").innerHTML="About the invention of the computer";
		document.getElementById("button2").innerHTML="About code syntax in Python";
		document.getElementById("image").src="random_fact.jpeg";
	}
	else if(document.getElementById("button2").innerHTML=="C and Assembly")
	{
		document.getElementById("h1").innerHTML="The language was too hard for the user, now he is sad and confused. And it somehow, in a magical way led to the apocalypse";
		document.getElementById("button1").innerHTML="RESTART";
		document.getElementById("button2").innerHTML="RESTART Please";
		document.getElementById("image").src="apocalypse.jpg";
	}
	else if(document.getElementById("button2").innerHTML=="About code syntax in Python")
	{
		document.getElementById("h1").innerHTML="Well, the user is a MEET student so he already knows it. now he is bored and you regret the time and effort you put into making this project. Go and make another project to please the user by hitting one of the buttons below";
		document.getElementById("button1").innerHTML="RESTART";
		document.getElementById("button2").innerHTML="RESTART Please";
		document.getElementById("image").src="go.png";
	}
	else if(document.getElementById("button2").innerHTML=="NO, I want to make something else")
	{
		document.getElementById("h1").innerHTML="Great, you made the right choice. Now be creative and come up with a good idea for a project! Good Luck!";
		document.getElementById("button1").innerHTML="RESTART";
		document.getElementById("button2").innerHTML="RESTART Please";
		document.getElementById("image").src="creativity.jpeg";
	}
	else if(document.getElementById("button2").innerHTML=="RESTART Please")
	{
		document.getElementById("h1").innerHTML="Do you want to make a project?";
		document.getElementById("button1").innerHTML="YES Of course!";
		document.getElementById("button2").innerHTML="NO I don't";
		document.getElementById("image").src="start.jpg";
	}
}

function option3()
{
	if(document.getElementById("h1").innerHTML=="Do you want to make a project?")
	{
		document.getElementById("h1").innerHTML='Welcome to your project maker in a "choose your own adventure" style.<br>Are you ready to start?';
		document.getElementById("button1").innerHTML="Of course I'm ready! I'm always ready!";
		document.getElementById("button2").innerHTML="I'm not ready but you don't really give me another choice";
		document.getElementById("image").src="let_the_games_began.png";
	}
	else if (document.getElementById("h1").innerHTML=="Too bad! you don't have a project and you should be sad about it! Now run before mjolnir gets you! The Ragnarok has began!")
	{
		document.getElementById("h1").innerHTML="You cannot escape Ragnarok!!!";
	}
	else if(document.getElementById("h1").innerHTML=="You cannot escape Ragnarok!!!")
	{
		document.getElementById("h1").innerHTML="Ok I see that you really want to go back and make a project so I will allow you, but remember: you cannot escape the Ragnarok!";
	}
	else if(document.getElementById("h1").innerHTML=="Ok I see that you really want to go back and make a project so I will allow you, but remember: you cannot escape the Ragnarok!"||document.getElementById("h1").innerHTML=="Great! choose your idea:")
	{
		document.getElementById("h1").innerHTML="Do you want to make a project?";
		document.getElementById("button1").innerHTML="YES Of course!";
		document.getElementById("button2").innerHTML="NO I don't";
		document.getElementById("image").src="start.jpg";
	}
	else if(document.getElementById("h1").innerHTML=="What will it be about?"||document.getElementById("h1").innerHTML=="What will your project be about?")
	{
		document.getElementById("h1").innerHTML="Great! choose your idea:";
		document.getElementById("button1").innerHTML="Make a project about CS";
		document.getElementById("button2").innerHTML="Make a project about making a project";
		document.getElementById("image").src="idea.jpeg";
	}
	else if(document.getElementById("h1").innerHTML=="What language are you going to teach?"||document.getElementById("h1").innerHTML=="What kind of facts are you going to give?")
	{
		document.getElementById("h1").innerHTML="What will it be about?";
		document.getElementById("button1").innerHTML="Help the user learn CS";
		document.getElementById("button2").innerHTML="Give random facts about CS";
		document.getElementById("image").src="CS.jpg";
	}
	else if(document.getElementById("h1").innerHTML=="The user learned a lot from you and he is happy! Good job for you!! Thor sends a storm to show his appreciation!"||document.getElementById("h1").innerHTML=="The language was too hard for the user, now he is sad and confused. And it somehow, in a magical way led to the apocalypse")
	{
		document.getElementById("h1").innerHTML="What language are you going to teach?";
		document.getElementById("button1").innerHTML="Python and Java Script";
		document.getElementById("button2").innerHTML="C and Assembly";
		document.getElementById("image").src="CS_languages.jpg";
	}
	else if(document.getElementById("h1").innerHTML=="The user now knows who invented the computer but he will definitely forget it by tomorrow so making this project was a waste of time. Instead you could have make global peace that will last forever but it's never too late to do it, start now"||document.getElementById("h1").innerHTML=="Well, the user is a MEET student so he already knows it. now he is bored and you regret the time and effort you put into making this project. Go and make another project to please the user by hitting one of the buttons below")
	{
		document.getElementById("h1").innerHTML="What kind of facts are you going to give?";
		document.getElementById("button1").innerHTML="About the invention of the computer";
		document.getElementById("button2").innerHTML="About code syntax in Python";
		document.getElementById("image").src="random_fact.jpeg";
	}
	else if(document.getElementById("h1").innerHTML=="Do you want to do exactly what I did and make a project about making a project in which you can make a project about making a project?"||document.getElementById("h1").innerHTML=="What kind of shop do you want it to be?")
	{
		document.getElementById("h1").innerHTML="What will your project be about?";
		document.getElementById("button1").innerHTML="Choose your own Adventure";
		document.getElementById("button2").innerHTML="Make a shop using HTML";
		document.getElementById("image").src="project.jpg";
	}
	else if(document.getElementById("h1").innerHTML=="NO! Do not do it! You should be creative and come up with your own idea! If Barak would see this, he would send a lightning right at you!"||document.getElementById("h1").innerHTML=="Great, you made the right choice. Now be creative and come up with a good idea for a project! Good Luck!")
	{
		document.getElementById("h1").innerHTML="Do you want to do exactly what I did and make a project about making a project in which you can make a project about making a project?";
		document.getElementById("button1").innerHTML="YES, exactly!";
		document.getElementById("button2").innerHTML="NO, I want to make something else";
		document.getElementById("image").src="fair_use.jpg";
	}
	else if(document.getElementById("h1").innerHTML=="Well, except from Barak and a few others, no one bought from you because most people don't really search for healthy food shops, but don't be sad, Barak sends thanks"||document.getElementById("h1").innerHTML=="You made Ted happy! now he will have more fireballs for the MEET summer and everyone will be happy! Thanks to you, there will soon be global peace! Go tell Barak, he will be very happy to know")
	{
		document.getElementById("h1").innerHTML="What kind of shop do you want it to be?";
		document.getElementById("button1").innerHTML="Healthy food shop";
		document.getElementById("button2").innerHTML="Fireball candy shop";
		document.getElementById("image").src="shop.png";
	}
}

//In this file I have 225 lines of code that make the game work (changes the buttons's text and the question's text depending on the button and the progress)