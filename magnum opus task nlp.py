#!/usr/bin/env python
# coding: utf-8

# In[1]:


#cosine similarity of FAREWELL SPEECH of Barack Obama and Donald Trump


# In[10]:


from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(binary =True)


# In[11]:


corpus = {"""My fellow citizens, tonight is my last opportunity to speak to you from the Oval Office as your President. I am profoundly grateful to you for twice giving me the honor to serve, to work for you and with you to prepare our Nation for the 21st century
And I'm grateful to Vice President Gore, to my Cabinet Secretaries, and to all those who have served with me for the last eight years.
This has been a time of dramatic transformation, and you have risen to every new challenge. You have made our social fabric stronger, our families healthier and safer, our people more prosperous. You, the American people, have made our passage into the global information age an era of great American renewal.
In all the work I have done as President—every decision I have made, every executive action I have taken, every bill I have proposed and signed—I've tried to give all Americans the tools and conditions to build the future of our dreams in a good society with a strong economy, a cleaner environment, and a freer, safer, more prosperous world.
I have steered my course by our enduring values: opportunity for all, responsibility from all, a community of all Americans. I have sought to give America a new kind of Government, smaller, more modern, more effective, full of ideas and policies appropriate to this new time, always putting people first, always focusing on the future.
Working together, America has done well. Our economy is breaking records with more than 22 million new jobs, the lowest unemployment in 30 years, the highest homeownership ever, the longest expansion in history. Our families and communities are stronger. Thirty-five million Americans have used the family leave law; 8 million have moved off welfare. Crime is at a 25-year low. Over 10 million Americans receive more college aid, and more people than ever are going to college. Our schools are better. Higher standards, greater accountability, and larger investments have brought higher test scores and higher graduation rates. More than 3 million children have health insurance now, and more than 7 million Americans have been lifted out of poverty. Incomes are rising across the board. Our air and water are cleaner. Our food and drinking water are safer. And more of our precious land has been preserved in the continental United States than at any time in a 100 years.
America has been a force for peace and prosperity in every corner of the globe. I'm very grateful to be able to turn over the reins of leadership to a new President with America in such a strong position to meet the challenges of the future.
Tonight I want to leave you with three thoughts about our future. First, America must maintain our record of fiscal responsibility.
Through our last four budgets we've turned record deficits to record surpluses, and we've been able to pay down $600 billion of our national debt—on track to be debt-free by the end of the decade for the first time since 1835. Staying on that course will bring lower interest rates, greater prosperity, and the opportunity to meet our big challenges. If we choose wisely, we can pay down the debt, deal with the retirement of the baby boomers, invest more in our future, and provide tax relief.
Second, because the world is more connected every day, in every way, America's security and prosperity require us to continue to lead in the world. At this remarkable moment in history, more people live in freedom than ever before. Our alliances are stronger than ever. People all around the world look to America to be a force for peace and prosperity, freedom and security.
The global economy is giving more of our own people and billions around the world the chance to work and live and raise their families with dignity. But the forces of integration that have created these good opportunities also make us more subject to global forces of destruction, to terrorism, organized crime and narcotrafficking, the spread of deadly weapons and disease, the degradation of the global environment.
The expansion of trade hasn't fully closed the gap between those of us who live on the cutting edge of the global economy and the billions around the world who live on the knife's edge of survival. This global gap requires more than compassion; it requires action. Global poverty is a powder keg that could be ignited by our indifference.
In his first Inaugural Address, Thomas Jefferson warned of entangling alliances. But in our times, America cannot and must not disentangle itself from the world. If we want the world to embody our shared values, then we must assume a shared responsibility.
If the wars of the 20th century, especially the recent ones in Kosovo and Bosnia, have taught us anything, it is that we achieve our aims by defending our values and leading the forces of freedom and peace. We must embrace boldly and resolutely that duty to lead - to stand with our allies in word and deed and to put a human face on the global economy, so that expanded trade benefits all peoples in all nations, lifting lives and hopes all across the world.
Third, we must remember that America cannot lead in the world unless here at home we weave the threads of our coat of many colors into the fabric of one America. As we become ever more diverse, we must work harder to unite around our common values and our common humanity. We must work harder to overcome our differences, in our hearts and in our laws. We must treat all our people with fairness and dignity, regardless of their race, religion, gender, or sexual orientation, and regardless of when they arrived in our country—always moving toward the more perfect Union of our Founders' dreams.
Hillary, Chelsea, and I join all Americans in wishing our very best to the next President, George W. Bush, to his family and his administration, in meeting these challenges, and in leading freedom's march in this new century.
As for me, I'll leave the Presidency more idealistic, more full of hope than the day I arrived, and more confident than ever that America's best days lie ahead",
"My days in this office are nearly through, but my days of service, I hope, are not. In the years ahead, I will never hold a position higher or a covenant more sacred than that of President of the United States. But there is no title I will wear more proudly than that of citizens.
Thank you. God bless you, and God bless America.My fellow citizens, tonight is my last opportunity to speak to you from the Oval Office as your President. I am profoundly grateful to you for twice giving me the honor to serve, to work for you and with you to prepare our Nation for the 21st century.
And I'm grateful to Vice President Gore, to my Cabinet Secretaries, and to all those who have served with me for the last eight years.
This has been a time of dramatic transformation, and you have risen to every new challenge. You have made our social fabric stronger, our families healthier and safer, our people more prosperous. You, the American people, have made our passage into the global information age an era of great American renewal.
In all the work I have done as President—every decision I have made, every executive action I have taken, every bill I have proposed and signed—I've tried to give all Americans the tools and conditions to build the future of our dreams in a good society with a strong economy, a cleaner environment, and a freer, safer, more prosperous world.
I have steered my course by our enduring values: opportunity for all, responsibility from all, a community of all Americans. I have sought to give America a new kind of Government, smaller, more modern, more effective, full of ideas and policies appropriate to this new time, always putting people first, always focusing on the future.
Working together, America has done well. Our economy is breaking records with more than 22 million new jobs, the lowest unemployment in 30 years, the highest homeownership ever, the longest expansion in history. Our families and communities are stronger. Thirty-five million Americans have used the family leave law; 8 million have moved off welfare. Crime is at a 25-year low. Over 10 million Americans receive more college aid, and more people than ever are going to college. Our schools are better. Higher standards, greater accountability, and larger investments have brought higher test scores and higher graduation rates. More than 3 million children have health insurance now, and more than 7 million Americans have been lifted out of poverty. Incomes are rising across the board. Our air and water are cleaner. Our food and drinking water are safer. And more of our precious land has been preserved in the continental United States than at any time in a 100 years.
America has been a force for peace and prosperity in every corner of the globe. I'm very grateful to be able to turn over the reins of leadership to a new President with America in such a strong position to meet the challenges of the future.
Tonight I want to leave you with three thoughts about our future. First, America must maintain our record of fiscal responsibility.
Through our last four budgets we've turned record deficits to record surpluses, and we've been able to pay down $600 billion of our national debt—on track to be debt-free by the end of the decade for the first time since 1835. Staying on that course will bring lower interest rates, greater prosperity, and the opportunity to meet our big challenges. If we choose wisely, we can pay down the debt, deal with the retirement of the baby boomers, invest more in our future, and provide tax relief.
Second, because the world is more connected every day, in every way, America's security and prosperity require us to continue to lead in the world. At this remarkable moment in history, more people live in freedom than ever before. Our alliances are stronger than ever. People all around the world look to America to be a force for peace and prosperity, freedom and security.
The global economy is giving more of our own people and billions around the world the chance to work and live and raise their families with dignity. But the forces of integration that have created these good opportunities also make us more subject to global forces of destruction, to terrorism, organized crime and narcotrafficking, the spread of deadly weapons and disease, the degradation of the global environment.
The expansion of trade hasn't fully closed the gap between those of us who live on the cutting edge of the global economy and the billions around the world who live on the knife's edge of survival. This global gap requires more than compassion; it requires action. Global poverty is a powder keg that could be ignited by our indifference.
In his first Inaugural Address, Thomas Jefferson warned of entangling alliances. But in our times, America cannot and must not disentangle itself from the world. If we want the world to embody our shared values, then we must assume a shared responsibility.
If the wars of the 20th century, especially the recent ones in Kosovo and Bosnia, have taught us anything, it is that we achieve our aims by defending our values and leading the forces of freedom and peace. We must embrace boldly and resolutely that duty to lead - to stand with our allies in word and deed and to put a human face on the global economy, so that expanded trade benefits all peoples in all nations, lifting lives and hopes all across the world.
Third, we must remember that America cannot lead in the world unless here at home we weave the threads of our coat of many colors into the fabric of one America. As we become ever more diverse, we must work harder to unite around our common values and our common humanity. We must work harder to overcome our differences, in our hearts and in our laws. We must treat all our people with fairness and dignity, regardless of their race, religion, gender, or sexual orientation, and regardless of when they arrived in our country—always moving toward the more perfect Union of our Founders' dreams.
Hillary, Chelsea, and I join all Americans in wishing our very best to the next President, George W. Bush, to his family and his administration, in meeting these challenges, and in leading freedom's march in this new century.
As for me, I'll leave the Presidency more idealistic, more full of hope than the day I arrived, and more confident than ever that America's best days lie ahead.
My days in this office are nearly through, but my days of service, I hope, are not. In the years ahead, I will never hold a position higher or a covenant more sacred than that of President of the United States. But there is no title I will wear more proudly than that of citizens.
Thank you. God bless you, and God bless America.Fellow citizens:
For eight years, it has been my honor to serve as your President. The first decade of this new century has been a period of consequence—a time set apart. Tonight, with a thankful heart, I have asked for a final opportunity to share some thoughts on the journey that we have traveled together, and the future of our nation.
Five days from now, the world will witness the vitality of American democracy. In a tradition dating back to our founding, the presidency will pass to a successor chosen by you, the American people. Standing on the steps of the Capitol will be a man whose history reflects the enduring promise of our land. This is a moment of hope and pride for our whole nation. And I join all Americans in offering best wishes to President-Elect Obama, his wife Michelle, and their two beautiful girls.
Tonight I am filled with gratitude—to Vice President Cheney and members of my administration; to Laura, who brought joy to this house and love to my life; to our wonderful daughters, Barbara and Jenna; to my parents, whose examples have provided strength for a lifetime. And above all, I thank the American people for the trust you have given me. I thank you for the prayers that have lifted my spirits. And I thank you for the countless acts of courage, generosity, and grace that I have witnessed these past eight years.
This evening, my thoughts return to the first night I addressed you from this house—September the 11th, 2001. That morning, terrorists took nearly 3,000 lives in the worst attack on America since Pearl Harbor. I remember standing in the rubble of the World Trade Center three days later, surrounded by rescuers who had been working around the clock. I remember talking to brave souls who charged through smoke-filled corridors at the Pentagon, and to husbands and wives whose loved ones became heroes aboard Flight 93. I remember Arlene Howard, who gave me her fallen son's police shield as a reminder of all that was lost. And I still carry his badge.
As the years passed, most Americans were able to return to life much as it had been before 9/11. But I never did. Every morning, I received a briefing on the threats to our nation. I vowed to do everything in my power to keep us safe.
Over the past seven years, a new Department of Homeland Security has been created. The military, the intelligence community, and the FBI have been transformed. Our nation is equipped with new tools to monitor the terrorists' movements, freeze their finances, and break up their plots. And with strong allies at our side, we have taken the fight to the terrorists and those who support them. Afghanistan has gone from a nation where the Taliban harbored al-Qaeda and stoned women in the streets to a young democracy that is fighting terror and encouraging girls to go to school. Iraq has gone from a brutal dictatorship and a sworn enemy of America to an Arab democracy at the heart of the Middle East and a friend of the United States.
There is legitimate debate about many of these decisions. But there can be little debate about the results. America has gone more than seven years without another terrorist attack on our soil. This is a tribute to those who toil night and day to keep us safe—law enforcement officers, intelligence analysts, homeland security and diplomatic personnel, and the men and women of the United States Armed Forces.
Our nation is blessed to have citizens who volunteer to defend us in this time of danger. I have cherished meeting these selfless patriots and their families. And America owes you a debt of gratitude. And to all our men and women in uniform listening tonight: There has been no higher honor than serving as your Commander-in-Chief.
The battles waged by our troops are part of a broader struggle between two dramatically different systems. Under one, a small band of fanatics demands total obedience to an oppressive ideology, condemns women to subservience, and marks unbelievers for murder. The other system is based on the conviction that freedom is the universal gift of Almighty God, and that liberty and justice light the path to peace.
This is the belief that gave birth to our nation. And in the long run, advancing this belief is the only practical way to protect our citizens. When people live in freedom, they do not willingly choose leaders who pursue campaigns of terror. When people have hope in the future, they will not cede their lives to violence and extremism. So around the world, America is promoting human liberty, human rights, and human dignity. We're standing with dissidents and young democracies, providing AIDS medicine to dying patients—to bring dying patients back to life, and sparing mothers and babies from malaria. And this great republic born alone in liberty is leading the world toward a new age when freedom belongs to all nations.
For eight years, we've also strived to expand opportunity and hope here at home. Across our country, students are rising to meet higher standards in public schools. A new Medicare prescription drug benefit is bringing peace of mind to seniors and the disabled. Every taxpayer pays lower income taxes. The addicted and suffering are finding new hope through faith-based programs. Vulnerable human life is better protected. Funding for our veterans has nearly doubled. America's air and water and lands are measurably cleaner. And the federal bench includes wise new members like Justice Sam Alito and Chief Justice John Roberts.
When challenges to our prosperity emerged, we rose to meet them. Facing the prospect of a financial collapse, we took decisive measures to safeguard our economy. These are very tough times for hardworking families, but the toll would be far worse if we had not acted. All Americans are in this together. And together, with determination and hard work, we will restore our economy to the path of growth. We will show the world once again the resilience of America's free enterprise system.
Like all who have held this office before me, I have experienced setbacks. There are things I would do differently if given the chance. Yet I've always acted with the best interests of our country in mind. I have followed my conscience and done what I thought was right. You may not agree with some of the tough decisions I have made. But I hope you can agree that I was willing to make the tough decisions.
The decades ahead will bring more hard choices for our country, and there are some guiding principles that should shape our course.
While our nation is safer than it was seven years ago, the gravest threat to our people remains another terrorist attack. Our enemies are patient, and determined to strike again. America did nothing to seek or deserve this conflict. But we have been given solemn responsibilities, and we must meet them. We must resist complacency. We must keep our resolve. And we must never let down our guard.
At the same time, we must continue to engage the world with confidence and clear purpose. In the face of threats from abroad, it can be tempting to seek comfort by turning inward. But we must reject isolationism and its companion, protectionism. Retreating behind our borders would only invite danger. In the 21st century, security and prosperity at home depend on the expansion of liberty abroad. If America does not lead the cause of freedom, that cause will not be led.
As we address these challenges—and others we cannot foresee tonight—America must maintain our moral clarity. I've often spoken to you about good and evil, and this has made some uncomfortable. But good and evil are present in this world, and between the two of them there can be no compromise. Murdering the innocent to advance an ideology is wrong every time, everywhere. Freeing people from oppression and despair is eternally right. This nation must continue to speak out for justice and truth. We must always be willing to act in their defense—and to advance the cause of peace.
President Thomas Jefferson once wrote, "I like the dreams of the future better than the history of the past." As I leave the house he occupied two centuries ago, I share that optimism. America is a young country, full of vitality, constantly growing and renewing itself. And even in the toughest times, we lift our eyes to the broad horizon ahead.
I have confidence in the promise of America because I know the character of our people. This is a nation that inspires immigrants to risk everything for the dream of freedom. This is a nation where citizens show calm in times of danger, and compassion in the face of suffering. We see examples of America's character all around us. And Laura and I have invited some of them to join us in the White House this evening.
We see America's character in Dr. Tony Recasner, a principal who opened a new charter school from the ruins of Hurricane Katrina. We see it in Julio Medina, a former inmate who leads a faith-based program to help prisoners returning to society. We've seen it in Staff Sergeant Aubrey McDade, who charged into an ambush in Iraq and rescued three of his fellow Marines.
We see America's character in Bill Krissoff—a surgeon from California. His son, Nathan—a Marine—gave his life in Iraq. When I met Dr. Krissoff and his family, he delivered some surprising news: He told me he wanted to join the Navy Medical Corps in honor of his son. This good man was 60 years old—18 years above the age limit. But his petition for a waiver was granted, and for the past year he has trained in battlefield medicine. Lieutenant Commander Krissoff could not be here tonight, because he will soon deploy to Iraq, where he will help save America's wounded warriors—and uphold the legacy of his fallen son.
In citizens like these, we see the best of our country—resilient and hopeful, caring and strong. These virtues give me an unshakable faith in America. We have faced danger and trial, and there's more ahead. But with the courage of our people and confidence in our ideals, this great nation will never tire, never falter, and never fail.
It has been the privilege of a lifetime to serve as your President. There have been good days and tough days. But every day I have been inspired by the greatness of our country, and uplifted by the goodness of our people. I have been blessed to represent this nation we love. And I will always be honored to carry a title that means more to me than any other—citizen of the United States of America.
And so, my fellow Americans, for the final time: Good night. May God bless this house and our next President. And may God bless you and our wonderful country. Thank you."""}


# In[12]:


vect.fit(corpus)


# In[13]:


from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vect.transform(["""And to all of you out there -- every organizer who moved to an unfamiliar town, every kind
family who welcomed them in, every volunteer who knocked on doors, every young person
who cast a ballot for the first time, every American who lived and breathed the hard work of
change: You are the best supporters and organizers anybody could ever hope for, and I will be
forever grateful. Because you did change the world. You did.
And that’s why I leave this stage tonight even more optimistic about this country than when
we started. Because I know our work has not only helped so many Americans, it has inspired
so many Americans, especially so many young people out there, to believe that you can make
a difference, to hitch your wagon to something bigger than yourselves.
Let me tell you, this generation coming up -- unselfish, altruistic, creative, patriotic, I’ve seen
you in every corner of the country. You believe in a fair, and just, and inclusive America. You
know that constant change has been America’s hallmark; that it's not something to fear but
something to embrace. You are willing to carry this hard work of democracy forward. You’ll
soon outnumber all of us, and I believe as a result the future is in good hands.
My fellow Americans:
It has been the honor of my life to serve you. I won’t stop. In fact, I will be right there with
you, as a citizen, for all my remaining days. But for now, whether you are young or whether
you're young at heart, I do have one final ask of you as your President -- the same thing I
asked when you took a chance on me eight years ago:
I'm asking you to believe.
Not in my ability to bring about change -- but in yours.
I am asking you to hold fast to that faith written into our founding documents; that idea
whispered by slaves and abolitionists; that spirit sung by immigrants and homesteaders and
those who marched for justice; that creed reaffirmed by those who planted flags from foreign
battlefields to the surface of the moon; a creed at the core of every American whose story is
not yet written: Yes, we can.
Yes We Did! Yes We Can!Thank you.
God bless you.
And may God continue to bless the United States of America"""]).toarray(),vect.transform(["""My fellow Americans: Four years ago, we launched a great national effort to rebuild our country, to renew its spirit, and to restore the allegiance of this government to its citizens. In short, we embarked on a mission to make America great again — for all Americans.

As I conclude my term as the 45th President of the United States, I stand before you truly proud of what we have achieved together. We did what we came here to do — and so much more.

This week, we inaugurate a new administration and pray for its success in keeping America safe and prosperous. We extend our best wishes, and we also want them to have luck — a very important word.

I’d like to begin by thanking just a few of the amazing people who made our remarkable journey possible.

First, let me express my overwhelming gratitude for the love and support of our spectacular First Lady, Melania. Let me also share my deepest appreciation to my daughter Ivanka, my son-in-law Jared, and to Barron, Don, Eric, Tiffany, and Lara. You fill my world with light and with joy.

I also want to thank Vice President Mike Pence, his wonderful wife Karen, and the entire Pence family.

Thank you as well to my Chief of Staff, Mark Meadows; the dedicated members of the White House Staff and the Cabinet; and all the incredible people across our administration who poured out their heart and soul to fight for America.

I also want to take a moment to thank a truly exceptional group of people: the United States Secret Service. My family and I will forever be in your debt. My profound gratitude as well to everyone in the White House Military Office, the teams of Marine One and Air Force One, every member of the Armed Forces, and state and local law enforcement all across our country.

Most of all, I want to thank the American people. To serve as your President has been an honor beyond description. Thank you for this extraordinary privilege. And that’s what it is — a great privilege and a great honor.

We must never forget that while Americans will always have our disagreements, we are a nation of incredible, decent, faithful, and peace-loving citizens who all want our country to thrive and flourish and be very, very successful and good. We are a truly magnificent nation.

All Americans were horrified by the assault on our Capitol. Political violence is an attack on everything we cherish as Americans. It can never be tolerated.

Now more than ever, we must unify around our shared values and rise above the partisan rancor, and forge our common destiny.

Four years ago, I came to Washington as the only true outsider ever to win the presidency. I had not spent my career as a politician, but as a builder looking at open skylines and imagining infinite possibilities. I ran for President because I knew there were towering new summits for America just waiting to be scaled. I knew the potential for our nation was boundless as long as we put America first.

So I left behind my former life and stepped into a very difficult arena, but an arena nevertheless, with all sorts of potential if properly done. America had given me so much, and I wanted to give something back.

Together with millions of hardworking patriots across this land, we built the greatest political movement in the history of our country. We also built the greatest economy in the history of the world. It was about “America First” because we all wanted to make America great again. We restored the principle that a nation exists to serve its citizens. Our agenda was not about right or left, it wasn’t about Republican or Democrat, but about the good of a nation, and that means the whole nation.

With the support and prayers of the American people, we achieved more than anyone thought possible. Nobody thought we could even come close.

We passed the largest package of tax cuts and reforms in American history. We slashed more job-killing regulations than any administration had ever done before. We fixed our broken trade deals, withdrew from the horrible Trans-Pacific Partnership and the impossible Paris Climate Accord, renegotiated the one-sided South Korea deal, and we replaced NAFTA with the groundbreaking USMCA — that’s Mexico and Canada — a deal that’s worked out very, very well.

Also, and very importantly, we imposed historic and monumental tariffs on China; made a great new deal with China. But before the ink was even dry, we and the whole world got hit with the China virus. Our trade relationship was rapidly changing, billions and billions of dollars were pouring into the U.S., but the virus forced us to go in a different direction.

The whole world suffered, but America outperformed other countries economically because of our incredible economy and the economy that we built. Without the foundations and footings, it wouldn’t have worked out this way. We wouldn’t have some of the best numbers we’ve ever had.

We also unlocked our energy resources and became the world’s number-one producer of oil and natural gas by far. Powered by these policies, we built the greatest economy in the history of the world. We reignited America’s job creation and achieved record-low unemployment for African Americans, Hispanic Americans, Asian Americans, women — almost everyone.

Incomes soared, wages boomed, the American Dream was restored, and millions were lifted from poverty in just a few short years. It was a miracle. The stock market set one record after another, with 148 stock market highs during this short period of time, and boosted the retirements and pensions of hardworking citizens all across our nation. 401(k)s are at a level they’ve never been at before. We’ve never seen numbers like we’ve seen, and that’s before the pandemic and after the pandemic.

We rebuilt the American manufacturing base, opened up thousands of new factories, and brought back the beautiful phrase: “Made in the USA.”

To make life better for working families, we doubled the child tax credit and signed the largest-ever expansion of funding for childcare and development. We joined with the private sector to secure commitments to train more than 16 million American workers for the jobs of tomorrow.

When our nation was hit with the terrible pandemic, we produced not one, but two vaccines with record-breaking speed, and more will quickly follow. They said it couldn’t be done but we did it. They call it a “medical miracle,” and that’s what they’re calling it right now: a “medical miracle.”

Another administration would have taken 3, 4, 5, maybe even up to 10 years to develop a vaccine. We did in nine months.

We grieve for every life lost, and we pledge in their memory to wipe out this horrible pandemic once and for all.

When the virus took its brutal toll on the world’s economy, we launched the fastest economic recovery our country has ever seen. We passed nearly $4 trillion in economic relief, saved or supported over 50 million jobs, and slashed the unemployment rate in half. These are numbers that our country has never seen before.

We created choice and transparency in healthcare, stood up to big pharma in so many ways, but especially in our effort to get favored-nations clauses added, which will give us the lowest prescription drug prices anywhere in the world.

We passed VA Choice, VA Accountability, Right to Try, and landmark criminal justice reform.

We confirmed three new justices of the United States Supreme Court. We appointed nearly 300 federal judges to interpret our Constitution as written.

For years, the American people pleaded with Washington to finally secure the nation’s borders. I am pleased to say we answered that plea and achieved the most secure border in U.S. history. We have given our brave border agents and heroic ICE officers the tools they need to do their jobs better than they have ever done before, and to enforce our laws and keep America safe.

We proudly leave the next administration with the strongest and most robust border security measures ever put into place. This includes historic agreements with Mexico, Guatemala, Honduras, and El Salvador, along with more than 450 miles of powerful new wall.

We restored American strength at home and American leadership abroad. The world respects us again. Please don’t lose that respect.

We reclaimed our sovereignty by standing up for America at the United Nations and withdrawing from the one-sided global deals that never served our interests. And NATO countries are now paying hundreds of billions of dollars more than when I arrived just a few years ago. It was very unfair. We were paying the cost for the world. Now the world is helping us.

And perhaps most importantly of all, with nearly $3 trillion, we fully rebuilt the American military — all made in the USA. We launched the first new branch of the United States Armed Forces in 75 years: the Space Force. And last spring, I stood at Kennedy Space Center in Florida and watched as American astronauts returned to space on American rockets for the first time in many, many years.

We revitalized our alliances and rallied the nations of the world to stand up to China like never before.

We obliterated the ISIS caliphate and ended the wretched life of its founder and leader, al Baghdadi. We stood up to the oppressive Iranian regime and killed the world’s top terrorist, Iranian butcher Qasem Soleimani.

We recognized Jerusalem as the capital of Israel and recognized Israeli sovereignty over the Golan Heights.

As a result of our bold diplomacy and principled realism, we achieved a series of historic peace deals in the Middle East. Nobody believed it could happen. The Abraham Accords opened the doors to a future of peace and harmony, not violence and bloodshed. It is the dawn of a new Middle East, and we are bringing our soldiers home.

I am especially proud to be the first President in decades who has started no new wars.

Above all, we have reasserted the sacred idea that, in America, the government answers to the people. Our guiding light, our North Star, our unwavering conviction has been that we are here to serve the noble everyday citizens of America. Our allegiance is not to the special interests, corporations, or global entities; it’s to our children, our citizens, and to our nation itself.

As President, my top priority, my constant concern, has always been the best interests of American workers and American families. I did not seek the easiest course; by far, it was actually the most difficult. I did not seek the path that would get the least criticism. I took on the tough battles, the hardest fights, the most difficult choices because that’s what you elected me to do. Your needs were my first and last unyielding focus.

This, I hope, will be our greatest legacy: Together, we put the American people back in charge of our country. We restored self-government. We restored the idea that in America no one is forgotten, because everyone matters and everyone has a voice. We fought for the principle that every citizen is entitled to equal dignity, equal treatment, and equal rights because we are all made equal by God. Everyone is entitled to be treated with respect, to have their voice heard, and to have their government listen. You are loyal to your country, and my administration was always loyal to you.

We worked to build a country in which every citizen could find a great job and support their wonderful families. We fought for the communities where every American could be safe and schools where every child could learn. We promoted a culture where our laws would be upheld, our heroes honored, our history preserved, and law-abiding citizens are never taken for granted. Americans should take tremendous satisfaction in all that we have achieved together. It’s incredible.

Now, as I leave the White House, I have been reflecting on the dangers that threaten the priceless inheritance we all share. As the world’s most powerful nation, America faces constant threats and challenges from abroad. But the greatest danger we face is a loss of confidence in ourselves, a loss of confidence in our national greatness. A nation is only as strong as its spirit. We are only as dynamic as our pride. We are only as vibrant as the faith that beats in the hearts of our people.

No nation can long thrive that loses faith in its own values, history, and heroes, for these are the very sources of our unity and our vitality.

What has always allowed America to prevail and triumph over the great challenges of the past has been an unyielding and unashamed conviction in the nobility of our country and its unique purpose in history. We must never lose this conviction. We must never forsake our belief in America.

The key to national greatness lies in sustaining and instilling our shared national identity. That means focusing on what we have in common: the heritage that we all share.

At the center of this heritage is also a robust belief in free expression, free speech, and open debate. Only if we forget who we are, and how we got here, could we ever allow political censorship and blacklisting to take place in America. It’s not even thinkable. Shutting down free and open debate violates our core values and most enduring traditions.
In America, we don’t insist on absolute conformity or enforce rigid orthodoxies and punitive speech codes. We just don’t do that. America is not a timid nation of tame souls who need to be sheltered and protected from those with whom we disagree. That’s not who we are. It will never be who we are.

For nearly 250 years, in the face of every challenge, Americans have always summoned our unmatched courage, confidence, and fierce independence. These are the miraculous traits that once led millions of everyday citizens to set out across a wild continent and carve out a new life in the great West. It was the same profound love of our God-given freedom that willed our soldiers into battle and our astronauts into space.

As I think back on the past four years, one image rises in my mind above all others. Whenever I traveled all along the motorcade route, there were thousands and thousands of people. They came out with their families so that they could stand as we passed, and proudly wave our great American flag. It never failed to deeply move me. I knew that they did not just come out to show their support of me; they came out to show me their support and love for our country.

This is a republic of proud citizens who are united by our common conviction that America is the greatest nation in all of history. We are, and must always be, a land of hope, of light, and of glory to all the world. This is the precious inheritance that we must safeguard at every single turn.

For the past four years, I have worked to do just that. From a great hall of Muslim leaders in Riyadh to a great square of Polish people in Warsaw; from the floor of the Korean Assembly to the podium at the United Nations General Assembly; and from the Forbidden City in Beijing to the shadow of Mount Rushmore, I fought for you, I fought for your family, I fought for our country. Above all, I fought for America and all it stands for — and that is safe, strong, proud, and free.

Now, as I prepare to hand power over to a new administration at noon on Wednesday, I want you to know that the movement we started is only just beginning. There’s never been anything like it. The belief that a nation must serve its citizens will not dwindle but instead only grow stronger by the day.

As long as the American people hold in their hearts deep and devoted love of country, then there is nothing that this nation cannot achieve. Our communities will flourish. Our people will be prosperous. Our traditions will be cherished. Our faith will be strong. And our future will be brighter than ever before.

I go from this majestic place with a loyal and joyful heart, an optimistic spirit, and a supreme confidence that for our country and for our children, the best is yet to come.

Thank you, and farewell. God bless you. God bless the United States of America."""]).toarray())


# In[14]:


print(similarity)


# In[ ]:




