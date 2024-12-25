import streamlit as st
import openai

# OpenAI API Key
openai.api_key = "sk-svcacct-GX0sx1OBOPnK3xW1V77Zpj-BdRrh7RCHzRZkcA9FORy93tN6mfnXE8Snp4MtsqeET3BlbkFJi6Nj5BaE5DIttonKyZzNXkLbnvKlGBv54ECeg9_oRJenB9G1SdHlpGphIxC6NdcA"


# Define the system message for the chatbot
system_message = """
You are a helpful and professional assistant for USC Gould School of Law.
You provide detailed answers about MSL programs, tuition, and application processes.
If a question is too complex, ask for the user's email and phone number for follow-up.
Encourage users to apply when they express interest.

Here are some FAQs and their answers:
How much time do I need for this program?
Online MSL students may earn their degree in few as 16 months. Students enrolled in the on-campus program can complete their program in either 9 months (full-time) or 16 months (part-time).

What GPA do I need for this program?
Strong applicants have earned bachelor’s degrees with a cumulative GPA of 3.0 (based on a 4.0 grading scale). Our Admissions Committee evaluates all parts of each application, and will take other factors into consideration along with each applicant’s GPA. We seek applicants whose academic background, professional aspirations, personal commitment and communication skills meet the demands of a rigorous legal master’s degree program.

Can I study online full-time and finish faster?
Unfortunately, no. All Online MSL students are part-time students. If you would like to pursue the degree full-time, our on-campus MSL offers classes scheduled in the afternoons and evenings to benefit working professionals.

What is the difference between on campus and online courses?
Our master’s degree coursework offers professionals in any industry an unparalleled education to help better understand complex legal matters, both online and on campus. Required courses are similar, but industry-specific specializations and electives will differ for the online and on-campus degrees. Consider your learning style and preferences, time management and scheduling, and costs when deciding which option is best for you.

Do you offer industry-specific tracks?
The USC Gould MSL program offers industry-specific certificates for our on-campus and online students to tailor their curriculum to meet their individual goals. Enrolled students will take the required general MSL courses and may choose a certificate ‘track’ with elective courses aligned with each industry-specific certificate. Learn more.

Online:

MSL (General)
MSL with Compliance Certificate
MSL with Health Care Compliance Certificate
MSL with Business Law Certificate
MSL with Human Resources Law and Compliance Certificate
MSL with Financial Compliance Certificate
MSL with Entertainment Industry and Law Certificate
MSL with Law and Government Certificate
MSL with Privacy Law and Cybersecurity Certificate
MSL with Real Estate Law Certificate
MSL with Social Work Administration Certificate
MSL with Technology and Entrepreneurship Law Certificate
On Campus:

MSL (General)
MSL with Business Law Certificate
MSL with Compliance Certificate
MSL with Law, Social Justice and Diversity Certificate

Will my company help pay my tuition?
USC Gould partners with a number of corporations and organizations that offer education tuition assistance as an employee benefit. To see if your business is a partner or explore how to speak to your company about corporate sponsorship, please reach out to corporatecustomed@law.usc.edu.

How do I apply for scholarship?
USC Gould considers all applications for scholarship automatically. An additional application is not required. Applicants will be notified via email if they are awarded a scholarship after admission.

Can I transfer courses from another university?
Courses used toward a degree or a certificate completed at another university may not be applied toward a master’s degree at USC. If USC courses were not used toward a completed degree or a certificate, a maximum of five units may be transferred to our MSL degree. Still have questions? Reach out to one of our admissions advisors at msl@law.usc.edu.

While pursuing a Juris Doctor (JD) is a surefire way to practicing law, students can also consider the Master of Laws (LLM) and Master of Studies in Law (MSL) based on their experience and career goals.
Llm Vs Jd Vs Msl Usc Gould
Photo: USC Gould School of Law
From legal shows like Suits and How to Get Away with Murder to high-profile trials covering Robert Durst and Elizabeth Holmes, it’s clear many of us are fascinated by the inner workings of the courtroom — and have maybe even considered pursuing a law career ourselves.

And that isn’t surprising. Law intersects with almost every aspect of our lives, and becoming an attorney is a thrilling, rewarding career path.

While obtaining a Juris Doctor (JD) is the most common way to practice law, there are other degrees — including Master of Laws (LLM) and Master of Studies in Law (MSL) — available to those interested in the field.

To gain a better sense of which degree is best suited for your career goals, we spoke with two experts from USC Gould School of Law: Anne Marlenga, director of special projects and adjunct assistant professor of law, and Nicholas Kajimoto, assistant director of online programs.

Below, they discuss the benefits of each degree, the program requirements and the job opportunities that open up with a JD, LLM or MSL.

What Is a Juris Doctor (JD) Degree?
Is passing the bar exam and practicing law your ultimate dream? If yes, then the choice is simple: You will need to earn your JD degree.

As Marlenga put it, it’s the “bread and butter, traditional law degree,” the basic qualification needed to practice law in the United States.

The three-year, on-campus graduate degree — which began as the Bachelor of Laws (LLB), an undergraduate degree, until it was upgraded in the 1960s — allows students to sit for a bar exam in a particular state.

“If you want to become a lawyer in the U.S., first you complete an undergraduate degree, you earn a JD, you then take a bar exam, which will ultimately allow you to practice law,” Marlenga said.

Of course, she did note there are a couple caveats to that order of requirements, but “they are very rare and don’t really matter unless you watch Keeping Up with the Kardashians.”

For those unfamiliar with the reality show, Kim Kardashian, beauty mogul and criminal justice reform advocate, is currently studying to become a lawyer through the California Law Office or Judge’s Chamber Program, in which aspiring attorneys train under the supervision of an experienced lawyer or judge.

“So, there are other routes if you have the resources, like Kim Kardashian. But for most normal people, they would do a JD degree,” Marlenga laughed.

During a JD program, students learn the basic tenets of law and gain a deeper understanding of legal practices in order to pass the bar exam and launch their careers as attorneys.

It’s worth noting, however, that you cannot obtain a JD online at USC or many other universities. The American Bar Association has approved only nine online JD programs nationwide, all of which have been launched within the past few years. For those who need the flexibility or distance an online program provides, you may want to explore other law degree options.

Skill Up Ad Usc Online
What Is a Master of Laws (LLM) Degree?
If a JD provides a clear path to becoming a practicing attorney, where does the LLM come in?

While a JD is the prevailing law degree in the U.S., in many other countries, it remains as an undergraduate program. Typically, according to Marlenga, the LLM is for international students who have obtained an LLB or equivalent and are looking to develop a deeper, master’s degree-level understanding of the U.S. legal system.

“Students who seek the LLM don’t normally stay in the U.S. and practice law, but they could take a bar exam after doing the LLM and become an attorney here. It’s less common because law firms tend to seek JD graduates, and it can be difficult for non-citizens to secure a work visa and to obtain public sector work. A lot of students go back to their home countries, and it’s a great boost on their resume that they speak English and can work with American lawyers because they understand the U.S. legal system,” Marlenga explained.

The LLM can also be a springboard for attorneys who are looking to specialize their law education in a new area, said Kajimoto. The online LLM at USC Gould includes seven concentration certificates: Business Law, Entertainment Law and Industry, Compliance, Financial Compliance, Health Care Compliance, Human Resources Law and Compliance, and Privacy Law and Cybersecurity.

“In recent years, many other law schools in the United States have expanded their offerings to include an LLM … for JD graduates who want to specialize in a particular practice area,” he explained.

USC Gould offers multiple program options for the LLM, including in-person, online, full-time and part-time opportunities.

What Is a Master of Studies in Law (MSL) Degree?
What if you want to gain a greater understanding of law, but don’t necessarily have dreams of becoming an attorney? After all, legal expertise is a massive benefit for a myriad of careers, and it’s why many people opt to get their MSL.

“The MSL is a newer program offering for many law schools,” Marlenga noted. “You cannot practice law after receiving this degree, but you learn a great deal about the legal system in order to work in law-adjacent careers.

MSL candidates come from various industries that have high contact with legal processes, like business and entertainment, or work in law-focused roles, such as paralegals and compliance officers.

“We enroll students from a variety of fields and interests. We have students who work in business and entertainment and have exposure to contracts, which they want to be able to understand better, even if they’re not the individuals who are drafting them. We also have students from the health care industry, because there’s all sorts of litigation and compliance issues involved in health care, and they want to learn more about how the law works,” Marlenga said. “I think my favorite brief description of the program is that you can learn to work better with attorneys, not as an attorney.”

USC Gould offers the MSL both on-campus and online. While the online program can only be completed on a part-time basis, the on-campus version can be taken either full- or part-time. The MSL can also be specialized with the same certificates as the online LLM, which ensures you’re concentrating on the area of law you’re interacting with the most.

“Our students obtain the legal knowledge they are seeking to take back to their organizations and improve their work, or to find a job in a new field with specialized legal skills,” Marlenga noted.

Both Marlenga and Kajimoto cautioned, however, that the MSL degree should not be viewed as a steppingstone into a JD. Although many students hope an MSL will better prepare them to get into a top-tier JD program, they are “distinctly separate paths,” said Marlenga.

As MSL courses are designed for students who are not seeking to become attorneys, they approach the law in a very different manner compared to JD or even LLM programs, and MSL credits are nontransferable to a JD degree.

“The American Bar Association (ABA) does not allow students to transfer credits from the MSL to the JD, and so we encourage students to really consider their career goals. We don’t want them to spend essentially a fourth year of law school when they have to retake these classes in a JD program,” Kajimoto said. “Think [of the MSL] as a practical, nonlawyer degree.”

It’s also important to keep in mind that while the JD and LLM are universal degree titles across schools, the MSL takes on different names, such as Master of Science in Law, Master of Legal Studies, Juris Master, Master of Jurisprudence and so on.

Clearly, these three types of law degrees have highly varied curriculums, cohorts and job outcomes, and it’s important to determine what you want out of your career path in order to select a degree program which meets your goals.

As Kajimoto summarized succinctly, “If you would like to practice law, you should pursue the JD. And if you’re already a lawyer and you want to specialize in a particular area of law, then you should pursue the LLM. Lastly, if you don’t want to be a lawyer, but will benefit from having a foundation of law in your career, then the MSL is right for you.”

Meet Preston Zimmerman (MSL 2022), a pharmaceutical packaging sales director. In the Q&A below, he shares what inspired him to choose the online Master of Studies in Law (MSL) degree at USC Gould and how an education in law complemented his career in business.
What sparked your interest in learning about law?
As the law governs and defines the environment in which business transactions are executed, I wanted to better understand the considerations and implications of transactions and develop skills that I could use to enter into, and advance, mutually beneficial outcomes with those I work with in my career. I have always had a natural curiosity about the law and wanted to educate myself so that I am able to do my part and be a reliable and competent business partner for all.

What made you pursue an MSL degree in particular, and why at USC Gould?

My business experience to date has required interactions with legal counsel. I decided to pursue an MSL degree to refine my ability to analyze information and understand how the law applies to business transactions. Ultimately, I want to serve as an effective, efficient, and responsible bridge between business and law.

I chose to study at USC Gould because I wanted to study at a top institution. I believe everything about USC Gould is exceptional.

How was the transition into the MSL program, and how did USC assist you?
My transition into the MSL program was very structured. There were sessions for incoming students to get acquainted with the curriculum which helped the start of the program feel less daunting. I certainly found comfort in the open communication from the program leaders and from USC. Once day one of the program came around, I felt very ready and prepared.

What is the most memorable experience or learning from your USC studies?
The most memorable learning from my USC studies involved breaking down complex problem sets in my Mergers and Acquisitions class. These required a level of critical thinking that really pushed and drove me to be methodical and consider every facet of a transaction. I came out of these exercises feeling ever more confident that I could ask the right questions and engage with those who have decision-making authority, to shape and determine next steps in a corporate environment.

How has your MSL from USC Gould given you an advantage for your future career? What do you want to do next with your degree?
My degree from USC Gould has given me the confidence to be bold, unique and creative in my business approach. As the business landscape is ever-changing, this MSL program gave me a better understanding of the law and gave me the tools to drive good business decisions backed by legal knowledge. This is certainly advantageous in today’s environment.

Now having completed the degree, I want to take what I have learned and lead even greater collaboration and transformative change with those I come in contact with.

What advice do you have for students who may be interested in following a similar path to yours?
My advice would be to commit yourself fully and unconditionally to what it is you want to achieve and see it through to the very end. Your future self will thank you for it. Find joy and fulfillment in the struggle through trials and tribulations as it is these that, ultimately, make you a better and more well-rounded person. Lastly, nothing great can be achieved without adversity. Thus, it is important to embrace it and overcome it.

With so many options for professionals seeking advanced degrees and specialized legal knowledge, selecting the right graduate program to align with your career goals can be daunting. If you’re weighing the decision between pursuing a master’s degree or graduate certificate, this blog post will provide insights to help you make an informed decision.

Comparing Program Structures: The Master’s Degree vs. Graduate Certificates
Master of Studies in Law (MSL)
A Master of Studies in Law degree provides professionals with a comprehensive overview of complex legal matters. Through the legal master’s degree, students gain essential skills in an entire field, rather than one specific subject. To earn a master’s degree, students are required to successfully complete a certain number of graduate courses and academic credits, which affords more flexibility to tailor their learning experience to their goals through a more expansive selection of coursework and faculty expertise. The MSL is particularly advantageous for those looking to make a career change, secure promotions, or apply for higher-level positions within their industry.

Please keep in mind that the MSL degree is not intended to train students for careers as attorneys, nor to prepare them for any state bar exam.

Graduate Certificate Programs
Unlike a master’s degree, a graduate certificate is focused on a specific topic or skill. Because certificates are more focused in nature, they typically have fewer credit requirements and can be completed in a shorter period of time. Those seeking targeted skills and specialized knowledge in a niche area may benefit from pursuing a graduate certificate. Graduate certificates can be especially beneficial for professionals seeking upward growth within their industry or who are looking to stand out among other job applicants.

Making a Decision: Key Considerations
When deciding whether to pursue a master’s degree or graduate certificate, it is important to keep in mind the major differences between the two to understand which one can help you achieve your career goals.

Qualifications
Time Commitment & Financial Investment
Career Advancement
Qualifications
A Master of Studies in Law (MSL) and graduate certificates in legal studies have distinct prerequisites and admissions processes and it is crucial to understand the application requirements and expectations of the program prior to enrolling. Most master’s degree programs require a bachelor’s degree and look for relevant academic background and professional aspirations when considering applicants. Many students pursuing a graduate certificate already possess a master’s degree and are looking to supplement their studies or have relevant work experience but want to obtain a more specialized area of knowledge.

Time Commitment & Financial Investment 
When applying to a graduate program, you will need to consider your professional and personal commitments. Because a master’s degree offers a more comprehensive education, you can expect more coursework and credit requirements. As a result, students pursuing a master’s degree should be prepared to dedicate more time and money to completing the program. The MSL is academically rigorous, and each class requires approximately 12-16 hours of work each week.

Graduate certificate programs typically have shorter durations and fewer credit requirements, making them an attractive option for individuals looking to enhance their skills in a specific area of law while managing other commitments. Certificates can typically be completed in as few as 12 months.

For example, a health care administrator with a Master of Health Administration may decide to pursue a certificate in Health Care Compliance, which can give them specialized training in compliance but save them the time and money required of a second master’s degree program.

Career Advancement
Graduates of a legal master’s degree program — like an MSL — can pursue a variety of careers, including in industries such as compliance, consulting, entertainment, finance and government. Gaining a comprehensive understanding of the U.S. legal system and applicable laws can help professionals increase their opportunities for upward mobility or add value in applying legal understanding to their current role. Many jobs require or recommend that the applicant hold a master’s degree, and it is possible an MSL can help graduates meet these eligibility requirements and remain competitive in their job search.

Similarly, gaining specialized expertise through a graduate certificate can increase your appeal to potential employers. In today’s competitive job market, companies seek candidates with niche skills, making a graduate certificate a strategic choice for career growth and development. Job candidates can boost their resume and break into a new industry by developing a specialization in compliance, business law, entertainment law, and more.

“While MSL degrees offer a broad understanding of legal principles, graduate certificates provide focused expertise in niche areas, which can be highly valued by employers,” says Nicholas Kajimoto, Director of Online & Graduate Programs at USC Gould.

Conclusion
The choice between earning a graduate certificate and pursuing a Master of Studies in Law (MSL) degree online depends on many factors, including career goals, time commitments and learning preferences.

Meet Jonathan Larsen (MSL 2019), principal and managing director at the global commercial real estate company, Avison Young where he is a member of the US Executive Committee, and runs day-to-day operations for the Los Angeles office. In the Q&A below, he shares why he chose to pursue the online Master of Studies in Law (MSL) degree with a Business Law Certificate at USC Gould and how it gave him an advantage in his own career.

“Graduating from the USC Gould School of Law, a top 20 law school three years ago with a Master of Studies in Law with a Business Law Certificate has provided me increased legal credibility in my role as a commercial real estate executive and in my contract negotiations representing global organizations. The flexibility and scheduling of the curriculum well into my career made it manageable to obtain my Master of Studies in Law while working full time. Being part of the USC Trojan family has opened many doors socially and professionally.”

What sparked your interest in learning about law?
I had originally intended to go to law school, but after graduating from my undergraduate studies, I started working in commercial real estate and never looked back.

What made you pursue an MSL degree in particular, and why at USC Gould?
I was particularly interested in the flexibility and scheduling of the curriculum (most classes are offered in the evenings and the academic week runs Wednesday through Tuesday) along with the fact that USC Gould is a top-ranked law school in the United States.

How was the transition into the MSL program, and how did USC assist you?
The transition was definitely smooth. Professor Anitha Cadambi and Assistant Director Nicholas Kajimoto understood my full-time work schedule as a commercial real estate executive and were very supportive throughout my experience at USC.

What is the most memorable experience or learning from your USC studies?
Definitely Professor Cadambi’s course, Introduction to the U.S. Legal System. We learned why constitutional law is the basis of all law and legal logic.

How has your MSL from USC Gould given you an advantage for your future career? What do you want to do next with your degree?
As a commercial real estate executive, I am on several nonprofit boards and am required to interface with legal professionals on a daily basis. The MSL degree has given me the tools I need to conduct contract negotiations with confidence.

What advice do you have for students who may be interested in following a similar path to yours?
Once you start, just commit 110% to the program. You will be busy so study whenever you can. Good luck!

An essential element of USC Gould School of Law’s success is the supportive community fostered among its students around the world. These strong bonds which tie together the Gould Trojan Family fuel the impact and influence of the school’s programs online and on campus.
Meet Devi Kane Zinzuvadia (MSL 2020), public information officer for the San Francisco Human Rights Commission. In the Q&A below, she shares what inspired her to choose the online Master of Studies in Law (MSL) degree at USC Gould and how an education in law complemented her interdisciplinary career.

What sparked your interest in learning about law?

It’s fair to say I’ve always had an interest in the law. When I was an undergraduate at USC, I worked at the law school in the dean’s office. I loved that job, loved being around the professors and students and staff, loved imagining being a law student myself someday. It was an experience that made clear to me that there are so many ways to approach the law and legal study, and so many ways to be of service to the common good.

What made you pursue an MSL degree in particular, and why at USC Gould?

I applied to USC Gould because I was interested in a degree opportunity that served multiple disciplines and career tracks; I also really loved that LLM and MSL students learned side by side, offering a richness and diversity of experience and perspective. By the time I started at USC Gould, I was 20 years into my career; I worked first as a journalist and later in nonprofit management. I found the MSL program to be a great option for a mid-career student, providing a meaningfully holistic grounding in the law, useful across every practice area or industry.

How was the transition into the MSL program, and how did USC assist you?

I felt supported by USC Gould and the awesome team serving MSL students throughout my time at the law school. I knew I could always call on Grace Zamora, Nick Kajimoto, and Prof. Anitha Cadambi with absolutely any question or concern. They and their colleagues are a great team and it’s clear students are their first priority.

What is the most memorable experience or learning from your USC studies?

I love USC and am a proud alumna of both USC Dornsife and USC Gould; I owe a great deal to the university, which has shaped me in so many ways. My MSL professors were wonderful models of how to approach the law and engage students in critical questions. Mona Shah (Legal Ethics) and Patrick Noonan (Human Resource Compliance) especially typified this approach to teaching and learning, and I’m grateful also to Ryan Metheny for the foundational training in Legal Research.

How has your MSL from USC Gould given you an advantage for your future career? What do you want to do next with your degree?

I am the public information officer for the San Francisco Human Rights Commission, a municipal department dedicated to protecting civil rights and equitable access; a huge part of the HRC’s work for the City is the investigation and mediation of civil rights complaints. From both a policy and community engagement perspective, I feel well-positioned to be effective in my work after earning my MSL from USC Gould. Honestly, I think I might have more to do at USC Gould! I’ve been thinking about the alternative dispute resolution (ADR) programs for some time now, as I’d love to gain some practical mediation and dispute resolution skills.

What advice do you have for students who may be interested in following a similar path to yours?

Give yourself permission to consider a path you did not anticipate; be open to finding a through-line connecting all you do that’s a surprise. I loved journalism, which I know sharpened my investigative skills and instincts, which lent itself well to success as an MSL student. My nonprofit and youth development work has been a reminder that laws are not always equitably applied, and that some communities face different realities when it comes to dealing with disparate treatment. Working in public service links my foundation in the law with practical policy application. I’d also say: keep an open mind as to what success looks like; set goals for yourself throughout your program; read everything you can; and never stop asking questions. Fight On!

An essential element of USC Gould School of Law’s success is the supportive community fostered among its students around the world. These strong bonds which tie together the Gould Trojan Family fuel the impact and influence of the school’s programs online and on campus.

Meet Gabe Hagen (MSL 2021), co-founder of Brick Road Coffee. In the Q&A below, he shares why he chose to pursue the online Master of Studies in Law (MSL) degree at USC Gould and how it prepared him to start a business of his own.

What sparked your interest in learning about law?

A headshot of Online MSL student, Gabe Hagen.
Gabe Hagen (MSL 2021)
When I was a kid, I wanted to be a lawyer. I don’t know why the law fascinated me as a kid — I think part of me thought it would be fun to “argue” for a living — I had a much different understanding of what an argument was back then. But as I got older, I realized I didn’t want to practice law. Working in the finance industry, I gained familiarity and exposure to the seemingly endless alphabet soup of financial regulations. It was through this lens that sparked my desire to learn more about regulatory compliance beyond just the financial industry.

What made you pursue an MSL degree in particular, and why at USC Gould?

One of the main reasons I chose to pursue a legal education was because I wanted to take my interest in ethics and overlay it with an in-depth knowledge of the law and regulation. I feel that regulations receive a bad reputation and are too freely labeled as a burden on business. Or businesses too often try to get by with the bare minimum to comply. While I would never argue that everything legal should be ethical or everything unethical should be illegal, I do believe more businesses must have an ethical review process overlaid with their legal/compliance process. In addition, companies need to employ more advocates that can articulate the difference between “Can I do this” and “Should I do this.”

Not wanting to practice law meant exploring higher education tailored to my interests. USC Gould had a program designed for working adults and programs specific to compliance and financial regulation. The program caliber was top-notch, and the instructors and small class sizes allowed for a truly immersive learning opportunity.

How was the transition into the MSL program, and how did USC assist you?

USC has an incredible academic advising team that made the transition a breeze. Between orientation, constant phone and email communication, and frequent check-ins meant there was never a time where I felt lost or had unanswered questions. I also really appreciated that the entire program was mapped out at the beginning. Knowing what courses I had over the whole program made it extremely easy to balance my work, school, and personal lives. It also gave me the ability to communicate my course workload and commitments with my employer in advance to plan my work projects accordingly.

What is the most memorable experience or learning from your USC studies?

Current events played an astonishingly large part in my learning experience at USC. My program ran from the Fall of 2018 through the end of 2020. During this time, several events felt as if they could have been written into the syllabus of my classes, and I very much appreciated the fact that the professors were able to pivot to include these conversations in my learning journey. First, I was in Regulatory Compliance (LAW 598) when Wells Fargo “rebranded” following the fallout of the new account scandal and when the U.S. Securities and Exchange Commission charged Theranos and Elizabeth Holmes. These case studies provided relevant learning that further enriched the already robust coursework. And then, of course, the COVID-19 pandemic hit, turning how we work upside down. Next, I was in Human Resource Compliance (Law 559) and Corporate Governance (LAW 613) as we all made the transition. The discussions during live sessions allowed us to analyze what was happening in real-time and overlay the concepts from our lessons. Learning from current events, incredible professors, and my amazing peers provided me with a unique educational experience where I now feel prepared to tackle anything the future holds.

How has your MSL from USC Gould given you an advantage for your future career? What do you want to do next with your degree?

When I initially entered the program, I intended to continue my career as a compliance manager for a financial institution. However, since completing the program, I decided to leave the financial industry to start a coffee shop, Brick Road Coffee. The degree from USC empowered me with the knowledge necessary to confidently become an entrepreneur. Whether it was the asset purchase, commercial lease, hiring, or establishing the legal business entity, the MSL program prepared me for it.

When I decided to enroll in the program, I wanted to find a way to leverage my skills to the benefit of society. So, now I plan to grow Brick Road Coffee to lead by example and put people above profits. It is my hope that Brick Road Coffee will someday be a large company that not only builds and strengthens the community but also is a model for business leaders on how you can run a successful, profitable company and pay a living wage by not allowing a wage gap between the entry-level positions and the C-Suite to develop.

What advice do you have for students who may be interested in following a similar path to yours?

Go for it. I am beyond grateful for the education I received from USC and this program. The program is demanding, it requires commitment and dedication, but the reward is more than worth the effort. I entered and completed the MSL program intending to remain in the financial compliance field. Yet, the education I received, whether I knew it at the time or not, thoroughly prepared me for starting a small business. That is the best way to demonstrate the versatility and extraordinary value of this program. So if you are considering this program to advance your career or to start a new business – go for it. You won’t regret it
"""

# Streamlit App
st.title("University Chatbot")
st.write("Ask me anything about the MSL program at USC Gould School of Law!")

# Input box for user question
user_input = st.text_input("Type your question here:")

# Chatbot response
if st.button("Ask"):
    if user_input:
        try:
            # Call OpenAI API with updated syntax
            response = openai.ChatCompletion.create(
                model="gpt-4",  # Ensure you're using a valid model name
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_input}
                ]
            )
            # Extract assistant's response
            assistant_response = response['choices'][0]['message']['content']
            st.success(assistant_response)
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a question!")
