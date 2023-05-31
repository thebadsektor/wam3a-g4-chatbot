from flask import Flask, request, render_template
import csv

app = Flask(__name__, template_folder='.')

def create_sample_csv():
    data = [
        ['What is your name?', 'My name is chatbot.'],
        ['Hello', 'Hello! Im a chatbot'],
        ['Hi', 'Hi Im a chatbot'],
        ['I want to shift', 'Contact the Registar Office for more information about shifting'],
        ['How are you?', 'Im doing well, thank you!'],
        ['Whats the weather today?', 'Im not a weather forecaster.'],
        ['Who created you?', 'I was created by a students in LSPU.'],
        ['How can I shift from  another course?', 'Contact the Registars Office offering the course for the application process.'],
        ['Shift a course', 'To shift a course you must go the Registarts Office'],
        ['Can a shift a course?', "Yes you can"],
        ['Is there an available list for all course?', 'Yes! Theres a lot'],
        ['Is there an gpa requirements to shift?', 'Yes there is'],
        ['Can I shift a course from one program to another?', 'It depends on program compatibility and department approval. Meet prerequisites and requirements for the new program.' ],
        ['What happens if my course shift request is denied?', 'Seek clarification from the department or academic advisor and explore alternative options'],
        ['Can I shift to a different program at the college?', 'Yes! depending on eligibility and program availability.'],
        ['How can I apply for a change of course/program at the college?','Submit an application for a change of course/program at the registar office'],
        ['When can I apply for a change of course/program at the college?','The application period for a change of course/program varies, check with the school registar for specific dates'],
        ['What are the requirements for shifting to a different department/major?','Requirements for shifting to a different department/major may vary, inquire with the school registar for details'],
        ['Can I shift to another college within the university? What is the process?','Shifting to another college within the university may be possible, follow the school registar process for transfers'],
        ['Are there any restrictions or limitations on shifting to a different program?','Restrictions or limitations on shifting to a different program may exist, consult with the school registrar for specific policies'],
        ['How many units can I transfer if I shift to a different course?','The number of units you can transfer when shifting to a different course depends on the school registrars policies'],
        ['Will my scholarship or financial aid be affected if I shift to a different program?','Scholarship or financial aid may be affected by shifting to a different program, check with the school registrar office for guidance'],
        ['Is there a specific GPA requirement for shifting to another course?','Shifting to a different program may have a specific time frame, inquire with the school registrar for applicable deadlines.'],
        ['Can I shift to a different program in the middle of the academic year, or is there a specific time frame for shifting?','Interviews or assessments may be part of the shifting process, contact the school registrar to understand their requirements'],
        ['Are there any interviews or assessments involved in the shifting process?','Shifting to a program with higher or lower admission requirements may be possible, consult with the school registrar for their policy'],
        ['Can I shift to a program that has a higher or lower admission requirement than my current program?','Fees or costs may be associated with shifting to a different course, inquire with the school registrar for details on any applicable charges'],
        ['Are there any fees or costs associated with shifting to a different course?','The time taken to process a shifting application varies, contact the school registrar for an estimate'],
        ['How long does it usually take to process a shifting application?','Completing prerequisite courses may be required before shifting to a specific program, consult with the school registrar for prerequisite information'],
        ['Are there any prerequisite courses I need to complete before shifting to a specific program?','Check with the school registrar for any prerequisite courses required before shifting to a specific program'],
        ['Can I shift to a program that has limited slots or is it subject to availability?','Shifting to a program may be subject to availability or limited slots, confirm with the school registrar'],
        ['Will my previous credits be counted towards my new program if I shift?','The school registrar will determine if your previous credits can be counted towards your new program when you shift.'],
        ['Are there any specific documents or forms I need to submit for the shifting process?','Inquire with the school registrar about specific documents or forms needed for the shifting process'],
        ['Can I request a meeting with an advisor or counselor to discuss my options before shifting?','Request a meeting with an advisor or counselor to discuss your options before shifting, if available'],
        ['What are the academic consequences of shifting to a different program?','The academic consequences of shifting to a different program may vary, consult with the school registrar for details'],
        ['Can I shift to a different program if I have already completed a significant portion of my current program?','Shifting to a different program after completing a significant portion of your current program may be possible, contact the school registra'],
        ['How will shifting to a different program affect my graduation timeline?','Shifting to a different program may affect your graduation timeline, consult with the school registrar for more information.'],
        ['Are there any specific deadlines for submitting a shifting application?','Check with the school registrar for specific deadlines regarding submitting a shifting application'],
        ['Are there any specific criteria or guidelines for selecting a new program to shift into?','The school registrar may have specific criteria or guidelines for selecting a new program to shift into, inquire with them'],
        ['Can I shift to a program in a different college or faculty within the university?','Shifting to a program in a different college or faculty within the university may be possible, confirm with the school registrar'],
        ['How will shifting to a different program affect my course sequencing and graduation requirements?','Shifting to a different program may impact your course sequencing and graduation requirements, consult with the school registrar for details'],
        ['Can I shift to a program that has different class schedules or is offered in a different format (e.g., online or evening classes)?','Shifting to a program with different class schedules or formats may be possible, contact the school registrar for more information.'],
        ['Are there any additional requirements or considerations for international students who wish to shift to a different program?','International students may have additional requirements or considerations when shifting to a different program, check with the school registrar.'],
        ['Can I shift to a program that requires specific skills or prerequisites that I may not have completed in my current program?','Shifting to a program requiring specific skills or prerequisites may have implications, consult the school registrar for guidance.'],
        ['Will I need to go through a new admission process for the new program I want to shift into?','Inquire with the school registrar if a new admission process is necessary for the program you want to shift into'],
        ['Can I shift to a program with a different degree level (e.g., from undergraduate to graduate)?','Shifting to a program with a different degree level may be possible, confirm with the school registrar'],
        ['How will shifting to a different program affect my housing arrangements or accommodations on campus?','Shifting to a different program may impact housing arrangements or accommodations on campus, consult the school registrar for guidance'],
        ['Can I shift to a program with a different language of instruction or in a different medium (e.g., from English to a foreign language)?','Shifting to a program with a different language of instruction or medium may be possible, inquire with the school registrar'],
        ['Are there any support services or resources available to assist students in the shifting process?','The school registrar or other support services may be available to assist students in the shifting process, reach out to them for help'],
        ['Can I shift to a program that has a higher or lower credit load than my current program?','Shifting to a program with a higher or lower credit load than your current program may have implications, consult the school registrar'],
        ['How will shifting to a different program affect my eligibility for extracurricular activities or sports teams?'],'Consider how shifting to a different program may affect your eligibility for extracurricular activities or sports teams, consult the school registrar.',
        ['Can I shift to a program with a different specialization or focus area within the same field of study?','Shifting to a program with a different specialization or focus area within the same field of study may be possible, contact the school registrar'],
        ['Will I need to provide a statement of purpose or explanation for why I want to shift to a different program?','Check with the school registrar if a statement of purpose or explanation is required for shifting to a different program.'],
        ['Can I shift to a program that has a different grading system or assessment methods than my current program?','Shifting to a program with a different grading system or assessment methods may have implications, consult the school registrar.'],
        ['How will shifting to a different program affect my access to research opportunities or internships?','Inquire with the school registrar about how shifting to a different program may affect your access to research opportunities or internships'],
        ['Can I shift to a program that requires additional prerequisites or qualifications beyond my current program?','Shifting to a program requiring additional prerequisites or qualifications beyond your current program may be possible, consult the school registrar.'],
        ['What should I consider before deciding to shift courses?','Consider various factors, such as your interests, goals, and academic requirements, before deciding to shift courses.'],
        ['How can I explore potential courses or programs to shift into?','Explore potential courses or programs by researching their curriculum, requirements, and career prospects.'],
        ['How do I determine if my credits will transfer to the new course?','Determine if your credits will transfer to the new course by contacting the school registrar or academic advisors.'],
        ['Are there any prerequisite courses I need to complete before shifting?','Check with the school registrar for any prerequisite courses you need to complete before shifting to a specific program.'],
        ['How can I prepare for the transition to a new course?','Prepare for the transition to a new course by familiarizing yourself with the syllabus, textbooks, and study materials.'],
        ['What steps should I take to ensure a smooth transition between courses?','Follow the necessary steps outlined by the school registrar to ensure a smooth transition between courses.'],
        ['How can I make the most of my academic transition and adapt to the new course?','Determine if your credits will transfer to the new course by contacting the school registrar or academic advisors'],
        ['What support services are available to assist students shifting courses?','Review syllabus, attend orientation, create a study plan, participate actively, seek help, connect with classmates'],
        ['How can I leverage my previous experiences and skills when shifting courses?','Academic advisors, tutoring centers, writing centers, counseling services, peer support groups.'],
        ['How can I stay motivated and focused during the process of shifting courses?','Set goals, break tasks, seek support, maintain balance, celebrate achievements, stay positive and resilient.'],
        ['How long does the program shifting process take?','The duration varies based on complexity and review process.'],
        ['Are there any mentorship programs available to assist students during the shifting process?','Mentorship programs may be available to support students during the shifting process.'],
        ['Can I shift to a program that offers study abroad opportunities?','Shifting to a program with study abroad opportunities depends on the specific programs offerings'],
        ['How will shifting to a different program affect my access to specific research facilities or labs?','Access to research facilities or labs may vary when shifting to a different program'],
        ['Are there any specialized scholarships or financial aid options for students shifting to certain programs?','Are there any specialized scholarships or financial aid options for students shifting to certain programs?'],
        ['There might be specialized scholarships or financial aid options for students shifting to specific programs.','There might be specialized scholarships or financial aid options for students shifting to specific programs.'],
        ['Can I shift to a program that has a cooperative education or internship component?','Some programs may have cooperative education or internship components for shifting students.'],
        ['What support is available for students experiencing difficulty in adjusting to the new program after shifting?','Support services are often available to help students adjust to the new program after shifting.'],
        ['Can I shift to a program that allows for flexible part-time or evening study options?','Flexibility in part-time or evening study options may vary depending on the program.'],
        ['How does shifting to a different program affect my eligibility for honors programs or academic societies?','Eligibility for honors programs or academic societies can be affected by shifting to a different program.'],
        ['Are there any opportunities for interdisciplinary studies or double majors when shifting programs?','Opportunities for interdisciplinary studies or double majors may vary for shifting students.'],
        ['Can I shift to a program that offers accelerated or combined degree options?','Some programs may have a focus on entrepreneurship or innovation for shifting students.'],
        ['Are there any opportunities for undergraduate research or collaborative projects when shifting to certain programs?','Opportunities for undergraduate research or collaborative projects may vary when shifting programs.'],
        ['Can I shift to a program that has a specific emphasis on community engagement or service learning?','Programs with a focus on community engagement or service learning may be options for shifting students.'],
        ['How does shifting to a different program affect my eligibility for study grants or funding opportunities?','Eligibility for study grants or funding opportunities can be influenced by shifting to a different program.'],
        ['Can I shift to a program that allows for self-designed or customized majors?','Customized majors or self-designed programs may be available for shifting students in certain cases.'],
        ['Are there any opportunities for cross-registration or taking courses from other colleges when shifting programs?','Cross-registration or taking courses from other colleges can vary for shifting students.'],
        ['How will shifting to a different program impact my eligibility for academic awards or recognition?','Shifting to a different program can impact eligibility for academic awards or recognition.'],
        ['Can I shift to a program that offers professional certification or licensure preparation?','Some programs may offer preparation for professional certification or licensure for shifting students.'],
        ['Are there any options for joint programs or partnerships with other institutions when shifting to certain programs?','Cross-registration or taking courses from other colleges can vary for shifting students.'],
        ['How will shifting to a different program impact my eligibility for academic awards or recognition?','Shifting to a different program can impact eligibility for academic awards or recognition.'],
        ['Can I shift to a program that offers professional certification or licensure preparation?','Some programs may offer preparation for professional certification or licensure for shifting students.'],
        ['Are there any options for joint programs or partnerships with other institutions when shifting to certain programs?','Joint programs or partnerships with other institutions can be options for shifting students in certain programs.'],
        ['How can I apply for a change of course/program at the college?','Contact the college administration for instructions on applying for a change of course/program.'],
        ['When can I apply for a change of course/program at the college?','Application timelines vary, so inquire with the college about specific dates for course/program changes.'],
        ['What are the requirements for shifting to a different department/major?','Requirements for shifting departments/majors may include certain GPA, prerequisites, or department-specific criteria.'],
        ['Can I shift to another college within the university? What is the process?','Check with the university to determine if shifting to another college is possible and follow their designated process.'],
        ['Are there any restrictions or limitations on shifting to a different program?','There might be restrictions or limitations on shifting programs, so consult the college for specific guidelines.'],
        ['How many units can I transfer if I shift to a different course?','The number of units you can transfer when shifting courses depends on the colleges credit transfer policy.'],
        ['Will my scholarship or financial aid be affected if I shift to a different program?','Shifting to a different program may impact your scholarship or financial aid, so verify with the colleges financial aid office.'],
        ['Is there a specific GPA requirement for shifting to another course?','GPA requirements for shifting to another course vary, so confirm with the college about any specific GPA criteria.'],
        ['Can I shift to a different program in the middle of the academic year, or is there a specific time frame for shifting?','Check if shifting during the academic year is allowed or if there is a specific time frame designated for shifting programs.'],
        ['Are there any interviews or assessments involved in the shifting process?','Interviews or assessments might be part of the shifting process, depending on the colleges policies.'],
        ['Can I shift to a program that has a higher or lower admission requirement than my current program?','Shifting to a program with higher or lower admission requirements depends on the college regulations.'],
        ['Are there any fees or costs associated with shifting to a different course?','Inquire with the college about any associated fees or costs related to shifting to a different course.'],
        ['How long does it usually take to process a shifting application?','Processing times for shifting applications vary, so consult the college for an estimate of the timeline.'],
        ['Are there any prerequisite courses I need to complete before shifting to a specific program?','Certain prerequisite courses may need to be completed before shifting to a specific program, so check with the department.'],
        ['Can I shift to a program that has limited slots or is it subject to availability?','Shifting to a program with limited slots could be subject to availability, depending on the colleges enrollment capacity.'],
        ['Will my previous credits be counted towards my new program if I shift?','Previous credits can be counted toward the new program, but it is contingent on the colleges credit transfer policy.'],
        ['Are there any specific documents or forms I need to submit for the shifting process?','The college may require specific documents or forms to be submitted for the shifting process, so inquire about the necessary paperwork.'],
        ['Can I request a meeting with an advisor or counselor to discuss my options before shifting?','Requesting a meeting with an advisor or counselor to discuss shifting options is typically possible and encouraged.'],
        ['What are the academic consequences of shifting to a different program?','Shifting to a different program can have academic consequences, such as additional requirements or adjusted graduation plans.'],
        ['Can I shift to a different program if I have already completed a significant portion of my current program?','The possibility of shifting to a different program after completing a significant portion of the current program depends on the colleges policies.'],
        ['How will shifting to a different program affect my graduation timeline?','Shifting to a different program can potentially affect your graduation timeline, so consult with the college to assess the impact.'],
        ['Are there any specific deadlines for submitting a shifting application?','Check with the college for specific deadlines regarding the submission of shifting applications.'],
        ['Are there any specific criteria or guidelines for selecting a new program to shift into?','The college may have criteria or guidelines in place for selecting a new program to shift into, so inquire about the requirements.'],
        ['Can I shift to a program in a different college or faculty within the university?','Shifting to a program in a different college or faculty within the university depends on the colleges regulations and availability.'],
        ['How will shifting to a different program affect my course sequencing and graduation requirements?','Shifting to a different program can impact course sequencing and graduation requirements, so consult with the department or advisor.'],
        ['Can I shift to a program that has different class schedules or is offered in a different format (e.g., online or evening classes)?','Programs with different class schedules or formats may be available for shifting, subject to the colleges offerings and policies.'],
        ['Are there any additional requirements or considerations for international students who wish to shift to a different program?','International students may have additional requirements or considerations when shifting to a different program, so contact the colleges international office for guidance.'],
        ['Can I shift to a program that requires specific skills or prerequisites that I may not have completed in my current program?','Shifting to a program with specific skills or prerequisites beyond your current program may require additional steps, such as completing the missing requirements.'],
        ['Will I need to go through a new admission process for the new program I want to shift into?','The need to go through a new admission process for the new program depends on the colleges policies and requirements.'],
        ['Can I shift to a program with a different degree level (e.g., from undergraduate to graduate)?','Shifting to a program with a different degree level (e.g., undergraduate to graduate) may have distinct guidelines and procedures, so consult with the college.'],
        ['How will shifting to a different program affect my housing arrangements or accommodations on campus?','Shifting to a different program may have implications for housing arrangements or accommodations, so discuss this with the relevant college offices.'],
        ['Can I shift to a program with a different language of instruction or in a different medium (e.g., from English to a foreign language)?','Shifting to a program with a different language of instruction or medium may be possible, depending on the colleges offerings and language requirements.'],
        ['Are there any support services or resources available to assist students in the shifting process?','Support services and resources are typically available to assist students in the shifting process, including academic advisors, counselors, and department representatives.'],
        ['Can I shift to a program that has a higher or lower credit load than my current program?','The credit load of a program may differ when shifting, depending on the specific requirements of the new program.'],
        ['How will shifting to a different program affect my eligibility for extracurricular activities or sports teams?','Shifting to a different program can potentially impact eligibility for extracurricular activities or sports teams, so inquire with the relevant college departments.'],
        ['Can I shift to a program with a different specialization or focus area within the same field of study?','Shifting to a program with a different specialization or focus area within the same field of study may be possible, depending on the colleges offerings and requirements.'],
        ['Will I need to provide a statement of purpose or explanation for why I want to shift to a different program?','The need for a statement of purpose or explanation when shifting to a different program depends on the college application requirements and guidelines.'],
        ['Can I shift to a program that has a different grading system or assessment methods than my current program?','Shifting to a program with a different grading system or assessment methods may entail adjusting to new evaluation criteria, so inquire about the specifics from the college.'],
        ['How will shifting to a different program affect my access to research opportunities or internships?','Shifting to a different program may impact access to research opportunities or internships, so discuss this with the department or relevant offices.'],
        ['Can I shift to a program that requires additional prerequisites or qualifications beyond my current program?','Programs requiring additional prerequisites or qualifications might necessitate completing the necessary requirements before shifting.'],
        ['What should I consider before deciding to shift courses?','Consider factors such as your interests, career goals, academic strengths, and potential opportunities when deciding to shift courses.'],
        ['How can I explore potential courses or programs to shift into?','Explore potential courses or programs by reviewing college catalogs, department websites, or consulting with advisors and faculty members.'],
        ['How do I determine if my credits will transfer to the new course?','To determine if your credits will transfer to the new course, consult with the colleges registrar or academic advisor.'],
        ['Are there any prerequisite courses I need to complete before shifting?','Check if there are any prerequisite courses you need to complete before shifting and plan accordingly.'],
        ['How can I prepare for the transition to a new course?','Prepare for the transition by familiarizing yourself with the new programs curriculum, requirements, and expectations.'],
        ['What steps should I take to ensure a smooth transition between courses?','Take steps such as meeting with advisors, attending orientation sessions, and actively engaging with the new program to ensure a smooth transition.'],
        ['How can I make the most of my academic transition and adapt to the new course?','Make the most of your academic transition by seeking support from faculty, connecting with peers, and taking advantage of available resources.'],
        ['What support services are available to assist students shifting courses?','Support services such as academic advising, counseling, and student organizations can assist you during the shifting process.'],
        ['How can I leverage my previous experiences and skills when shifting courses?','Leverage your previous experiences and skills by identifying transferable skills and knowledge applicable to the new program.'],
        ['How can I stay motivated and focused during the process of shifting courses?','Stay motivated and focused during the process of shifting courses by setting goals, seeking support when needed, and maintaining a positive mindset.'],
        ['Can shifters participate in study abroad or exchange programs during enrollment?','Yes, as long as the school allows it'],
        ['What types of academic accommodations are available for shifters during enrollment?','Accommodations could include things like flexible scheduling, alternative testing methods, or modified assignments to accommodate their unique circumstances.'],
        ['Can shifters choose their preferred courses or subjects during the enrollment process?','Shifters should generally have the ability to choose their preferred courses or subjects during the enrollment process, similar to non-shifters. However, specific course availability may depend on factors such as scheduling and prerequisites.'],
        ['Are there any possibilities for shifters to demonstrate their skills or talents while enrolled at the school?','Shifters may have opportunities to showcase their skills or talents while enrolled at the school. This could include participating in performances, competitions, or joining relevant clubs or organizations that allow them to express their abilities.'],
        ['Are there any specific legal considerations or rights for shifters during the enrollment process?','There may be specific legal considerations or rights for shifters during the enrollment process. These could include protections against discrimination based on their shapeshifting abilities or accommodations mandated by disability laws, depending on how their abilities are categorized.'],
        ['Can I shift enrollment if I have previously been expelled from another school?','Moving enlistment might be liable to a survey of past disciplinary activities. Before making a decision, the school may take into account the circumstances surrounding the expulsion and other relevant factors.'],
        ['Are there any specific requirements for shifting enrollment for students from homeschooling?','The school and district in which a homeschooling student attends may have different enrollment requirements. For specific instructions contact the school administration'],
        ['Will I have to start the academic year over if I shift enrollment in the middle of the year?','In order to determine the appropriate grade placement, shifting enrollment in the middle of the academic year may necessitate an assessment and evaluation of your previous coursework. The school organization can direct you through this cycle'],
        ['Can I shift enrollment if I have already graduated from high school?','Moving enlistment after secondary school graduation is normally not pertinent as it ordinarily relates to understudies who are as yet signed up for a K-12 school system.'],
        ['How will shifting enrollment affect my eligibility for scholarships or financial aid?','Scholarships and financial aid may be affected by changes in enrollment. Talk with the school monetary guide office to comprehend what moving enlistment can mean for your qualification for monetary help.'],
        ['Can I shift enrollment if I have a pending legal case or probationary status?',' Forthcoming legitimate cases or trial status might influence moving enlistment. Its best to let the school know about any legal issues and ask the administration for advice on enrolling.'],
        ['Are there any specific requirements for shifting enrollment for students with English as a second language?',' Schools frequently have explicit projects and backing for understudies with English as a second language who wish to move enlistment. Contact the school English language student office for explicit guidelines.'],
        ['Will my transportation options change if I shift enrollment?','Because the new school may have different policies and locations, so shifting enrollment may affect transportation options. Ask the school organization or transportation division for transportation courses of action data.'],
        [' Can I shift enrollment if I have an individualized education plan (IEP)?','For students with an individualized education plan (IEP), shifting enrollment may necessitate additional considerations. For specific instructions and assistance, get in touch with the school special education department.'],
        ['Are there any specific academic or behavioral requirements for shifting enrollment?','A few schools might have an explicit scholar or conduct prerequisites for moving enlistment. Ask the school organization about their rules for enlistment.'],
        ['Can I shift enrollment if I am a foster child or in the custody of a guardian?',' If a student or foster child is in a guardian custody, changing their enrollment may require additional paperwork or procedures. For specific instructions and assistance, get in touch with the school administration.'],
        ['What is the process for notifying my current school about my intent to shift enrollment?',' A crucial step is informing your current school of your intention to switch schools. Most of the time, you need to send a letter to the school administration.'],
        ['Can I shift enrollment if I am currently on academic probation at my current school?','Your academic standing may be reviewed and evaluated if you change schools while on probation. The school organization will give direction on the interaction and prerequisites.'],
        ['Are there any specific deadlines for submitting the required documents for shifting enrollment?','It is essential to adhere to the submission deadlines for shifting enrollment-related documents. Your application processing time may be impacted if you submit it late.'],
        ['Can I shift enrollment if I have already applied to colleges or universities?','Most of the time, changing enrollment has no effect on applications to colleges or universities. Notwithstanding, it is prudent to illuminate the organizations you have applied to about any progressions in your instructive status.'],
        ['Will shifting enrollment affect my class rank or honor roll status?','Moving enlistment might affect your class rank or honor roll status. Contact the school organization for data on what moving enlistment means for these scholarly acknowledgments.'],
        ['Are there any specific requirements for shifting enrollment for students with medical conditions or disabilities?','Students with disabilities or medical conditions who wish to change schools frequently have special requirements and support. Contact the school custom curriculum division or advising office for explicit directions and facilities.'],
        ['Can I shift enrollment if I am currently serving a suspension at my current school?','The receiving school may examine your enrollment change while you are serving a suspension at your current school.'],
        ['What is the policy for shifting enrollment for students who have been expelled from another school?','The policy for students who have been expelled from another school varies from school to school and district to district. Uncovering your past removal during the application interaction and giving any pertinent documentation is essential.'],
        ['Can I shift enrollment if I have been involved in a disciplinary incident at my current school?','A review of disciplinary incidents at your current school may apply to changing enrollment. The seriousness and recurrence of the episodes might be considered during the enlistment cycle. Accurate information and any necessary explanations are essential.'],
        ['Are there any specific requirements for shifting enrollment for students with advanced placement (AP) credits?','Moving enlistment necessities for understudies with cutting-edge arrangement (AP) credits can change. AP credits may be accepted by some schools, while other schools may use their own assessment or placement tests to determine which credits should be transferred. For specific information regarding AP credit policies, contact the school administration.'],
        ['Will shifting enrollment affect my graduation timeline or requirements?','Moving enlistment might influence your graduation timetable or prerequisites. It is fundamental to examine your scholastic advancement and graduation plan with the school organization to guarantee smooth progress.'],
        ['Can I shift enrollment if I am currently enrolled in a specialized program at my current school?','It may depend on availability and program-specific requirements to switch enrollment to a specialized program at the receiving school. For specific guidelines and instructions, get in touch with the school administration or program coordinator.'],
        ['Are there any specific requirements for shifting enrollment for students with behavioral or emotional support needs?','Dependent on the school resources and support services, shifting enrollment requirements for students with behavioral or emotional support needs can vary. For specific instructions and accommodations, contact the school counseling or special education department.'],
        ['Can I shift enrollment if I am currently enrolled in a private school?','Moving enlistment from a tuition-based school follows comparable methods to moving from different schools. However, additional procedures and documentation might be required. For specific instructions and requirements for moving from a private school, contact the school administration.'],
        ['Are there any specific programs or courses that are not available for shifting enrollment?','There may be limited availability or specific admission requirements for some specialized programs or courses, which could affect changing enrollment. Check with the school to see if such programs are offered.'],
        ['Do I need to provide a letter of recommendation for shifting enrollment?','Contingent upon the school strategies, you could possibly have to give a letter of suggestion to moving enlistment. Check with the school in regard to their particular necessities.'],
        ['How will my courses and credits transfer if I shift enrollment?','Schools have different policies regarding credit and course transfer. The getting school will ordinarily assess your scholastic records and decide how your courses and credits will be moved.'],
        ['Are there any specific criteria for shifting enrollment for international students?','For international students who are changing their enrollment, there may be additional requirements, like proof of a visa and language proficiency tests. For specific instructions, it is essential to get in touch with the school international student office.'],
        ['Can I visit the school and meet with teachers before completing the shifting enrollment process?','Before completing the shifting enrollment process, it is frequently possible to visit the school and meet with teachers. Make arrangements to visit the school and inquire about their visitation policies.'],
        ['Will I need to take an entrance exam or assessment for shifting enrollment?','For changing enrollment, an entrance exam or assessment may be required, depending on the policies of the school. Find out more about the school assessment procedures by contacting them.'],
        ['Are there any specific requirements for shifting enrollment into a magnet or specialized program?','Moving enlistment into a magnet or particular projects might have explicit necessities, like tryouts, meetings, or portfolio entries. Check with the school to find out how to apply for these programs.'],
        ['How will shifting enrollment affect my eligibility for extracurricular activities or sports?','Moving enlistment can affect your qualification for extracurricular exercises or sports. For information on the school policies regarding shifting student participation, check with the athletic department.'],
        ['Can I request a transfer to a specific school within the district through shifting enrollment?',' Subject to availability and district policies, it may be possible to shift enrollment to a specific school within the district. Contact the school region office for more data.'],
        ['Is there a limit to the number of students who can shift enrollment in a given year?','The capacity and policies of the school determine the maximum number of students who can change their enrollment. The school organization can give explicit data about enlistment limits.'],
        ['Can I submit additional supporting documents or letters of recommendation from teachers or?','Your application for shifting enrollment can be strengthened with additional supporting documents or letters of recommendation. It is recommended that these documents be submitted during the school application process.'],
        ['How does the school handle the assessment and placement of students who are shifting enrollment, particularly in regard to academic subjects?','The school procedures will determine how students with changing enrollment will be assessed and placed. They might look over your academic records, take tests, or give language proficiency tests to figure out where you should go.'],
        ['Can I request a tour of the school facilities, such as the library, science labs, or art studios, before completing the shifting enrollment process?','Prospective students can take a tour of the facilities at many schools. Before completing the shifting enrollment process, it is recommended to contact the school administration and request a tour to familiarize yourself with the facilities.'],
        ['Are there any specific steps or procedures in place for addressing potential conflicts or issues between shifters and existing students at the new school?','There are policies and procedures in place at schools to deal with disagreements or problems between shifters and current students. They might have programs for peer mediation, counseling, or disciplinary action in place to deal with these kinds of situations.'],
        ['Can I shift enrollment if I am currently under a court-ordered educational arrangement, such as probation or alternative schooling?','Moving enlistment while under a court-requested instructive game plan might have explicit contemplations. Its critical to let the school administration know about your situation and to follow the courts instructions.'],




    ]
    
    with open('responses.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
        

def load_responses():
    responses = []
    with open('responses.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            responses.append({'question': row[0], 'answer': row[1]})
    return responses

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    response = get_response(user_message, responses)
    return {'response': response}

def get_response(user_message, responses):
    for row in responses:
        if user_message.lower() in row['question'].lower():
            return row['answer']
    return "Sorry, I don't have an answer for that."
if __name__ == '__main__':
    responses = load_responses()
    app.run(debug=True)
    