from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set title
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, 'Alarape Abdulwahab Resume', ln=True, align='C')

# Add contact details
pdf.set_font('Arial', '', 12)
pdf.ln(10)
pdf.cell(200, 10, 'Computer Engineering Student | CyberSecurity | Aspiring Ethical Hacker', ln=True, align='C')
pdf.cell(200, 10, 'Phone: +234-8129974838 | Email: abisolaadewuyi@gmail.com', ln=True, align='C')
pdf.cell(200, 10, 'LinkedIn: www.linkedin.com/in/alarape-abdulwahab2467', ln=True, align='C')
pdf.cell(200, 10, 'Location: Lagos, Nigeria', ln=True, align='C')

# Add section: SUMMARY
pdf.ln(10)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'SUMMARY', ln=True)

pdf.set_font('Arial', '', 12)
summary_text = '''
Highly motivated and detail-oriented Computer Engineering student with a passion for Cybersecurity and Ethical 
Hacking. Experienced in penetration testing, vulnerability assessment, and network security. Proficient in automating 
cybersecurity tasks with Python and implementing encryption algorithms to ensure data security. Seeking an internship 
opportunity to apply and further develop my skills in a real-world cybersecurity environment.
'''
pdf.multi_cell(0, 10, summary_text)

# Add section: EXPERIENCE
pdf.ln(5)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'EXPERIENCE', ln=True)

pdf.set_font('Arial', 'I', 12)
pdf.cell(0, 10, 'IT Support Intern - Lychee Integrated Solutions Limited', ln=True)
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'April 2024 – May 2025 | Ketu, Lagos', ln=True)
experience1_text = '''
- Conducted vulnerability assessments and penetration tests on web applications and networks.
- Identified and reported security flaws, providing remediation recommendations.
- Collaborated with the security team to improve the overall security posture.
- Assisted in troubleshooting hardware and software issues, and monitored network performance.
'''
pdf.multi_cell(0, 10, experience1_text)

pdf.set_font('Arial', 'I', 12)
pdf.cell(0, 10, 'Siwes Placement - Lychee Integrated Solutions Limited', ln=True)
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'February 2023 – June 2023 | Ketu, Lagos', ln=True)
experience2_text = '''
- Supported network configuration and monitored network performance.
- Assisted in user account management and routine system maintenance.
'''
pdf.multi_cell(0, 10, experience2_text)

# Add section: EDUCATION
pdf.ln(5)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'EDUCATION', ln=True)

pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'National Diploma in Computer Engineering - Yaba College of Technology', ln=True)
pdf.cell(0, 10, 'April 2022 – February 2024 | Yaba, Lagos', ln=True)

# Add section: CERTIFICATIONS
pdf.ln(5)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'CERTIFICATIONS', ln=True)

certifications_text = '''
- CYBERSEK Certified AppSec Pentester (CCAP) – Passed
- Google IT Support Professional Certificate – Coursera
- Google CyberSecurity Professional Certificate – Coursera
- Mastercard CyberSecurity Job Simulation – Completed
- JPMorgan Chase & Co. CyberSecurity Job Simulation – Completed
- Basic Life Support (BLS) Provider
'''
pdf.multi_cell(0, 10, certifications_text)

# Add section: SKILLS
pdf.ln(5)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'SKILLS', ln=True)

skills_text = '''
Tools & Technologies: Kali Linux, Wireshark, Burp Suite, Metasploit, Nmap, Nessus
Programming Languages: Python, SQL
Operating Systems: Linux, Windows
Soft Skills: Problem Solving, Team Collaboration
'''
pdf.multi_cell(0, 10, skills_text)

# Add section: PROJECTS
pdf.ln(5)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'PROJECTS', ln=True)

projects_text = '''
1. Multi-Algorithm Text Encryption Project (January 2024 – July 2024)
- Developed a Python application to encrypt and decrypt text using AES, DES, and RSA algorithms.
- Demonstrated secure data handling and automated encryption for sensitive information.

2. Automating Cybersecurity Tasks with Python (February 2024 – July 2024)
- Automated network vulnerability scanning using Nmap, log analysis for anomaly detection, and threat intelligence gathering using public APIs.

3. Capture The Flag (CTF) Challenges (Various Platforms)
- Participated in challenges on Hack The Box and TryHackMe, solving problems related to web exploitation, cryptography, and forensics.

4. Network Intrusion Detection System (January 2024)
- Developed a network intrusion detection system using Snort.
- Implemented detection rules for various types of network attacks.

5. Secure File Transfer Application (March 2024)
- Developed a secure file transfer application using Python with encryption to ensure data confidentiality and integrity during transmission.

6. Vulnerability Assessment and Penetration Testing on Axia.Africa (June 2024)
- Conducted a comprehensive vulnerability assessment using Nessus on Axia.Africa.
- Drafted a detailed report including vulnerability summary, impact analysis, and incident response plan.
'''
pdf.multi_cell(0, 10, projects_text)

# Add section: COURSES
pdf.ln(5)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'COURSES', ln=True)

courses_text = '''
- Accounting Class – Topics on Fixed Assets, FIFO, LIFO, WAV (Weighted Average), and Asset Management
- Cybersecurity Training – Axia Africa
'''
pdf.multi_cell(0, 10, courses_text)

# Add section: LANGUAGES
pdf.ln(5)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'LANGUAGES', ln=True)

languages_text = '''
- English: Native
- Arabic: Intermediate
- Spanish: Beginner
'''
pdf.multi_cell(0, 10, languages_text)

# Save the PDF to file
pdf.output("Alarape_Abdulwahab_Resume.pdf")
