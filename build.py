import jinja2

data = {
    "relevant_achievements": [
        " Designed, implemented and tested an 8 channel digiitzer system for a wideband phased array. 180 MSPS x 8 channel capture capability provided full bandwidth data (2.9 GB/sec) to a high performance processing PC. Implemented multi-threaded data capture and processing software in C to perform signal detection and geolocation.",
        "Created, tested, and deployed Windows-based control software and user interface for a complex tactical RF sensor system, including MySQL data storage back-end, Java operator interface, and multi-threaded real-time data processing module in C.",
        "Wrote linux-based data mining tools to extract information from the topology and structure of complex networks.",
        "Implemented a C compiler, including parser, AST generation, optimizer, and x86 code emission.",
        "Designed, realized and optimized embedded DSP/control application in an proof-of-concept sensing system. Maximized system availability and maintainability by providing a complete set of system self diagnostics. Optimized system performance to exceed customer requirements, leading to success and expansion of initial contract.",
        "Designed and implemented Windows-based control software and FPGA hardware command interface to directly control functions of concurrently designed RF circuit boards. Successfully designed and implemented a custom serial control protocol over USB enable out-of-band troubleshooting, testing and calibration of RF synthesizer and reciever modules.",
        "Developed software for a Xilinx microcontroller/FPGA device to communicate simultaneously with 32 aircraft gyroscope modules and interface with a networked desktop computer for testing and calibration purposes.",
        "Designed and implemented a high speed analog data acquisition system as a PC104 expansion card, including FPGA programming, PCB layout, and Linux driver programming.",
        "Implemented software for autonomous mobile coordinated robotics system to locate an object within a search area.",
        "Designed, analyzed and constructed Ku-band polarization steerable feed for airborne high power satellite communications.",
    ],
    "jobs": [
        {
            "title": "Lead software engineer",
            "org": "Othram",
            "org_url": "https://othram.com",
            "date": "October 2018 - present",
            "location": "Remote",
            "details": [
                "...",
                "...."
            ]
        },

        {
            "title": "Lead software engineer",
            "org": "Gene By Gene / Family Tree DNA",
            "org_url": "https://genebygene.com",
            "date": "July 2013 - September 2018",
            "location": "Remote",
            "details": [
                "...",
                "...."
            ]
        },

        {
            "title": "Lead software engineer",
            "org": "Arpeggi, Inc",
            "org_url": "https://arpeggi.com",
            "date": "January 2013 - July 2013",
            "location": "Austin, TX",
            "details": [
                "",
                ""
            ]
        },

        {
            "title": "Software engineer",
            "org": "Virginia Bioinformatics Institute",
            "org_url": "",
            "date": "March 2012 - January 2013",
            "location": "Remote",
            "details": [
                "",
                ""
            ]
        },

        {
            "title": "Design Engineer",
            "org": "Invertix Corporation",
            "org_url": "http://www.invertix.com",
            "date": "January 2008 to May, 2011",
            "location": "Las Cruces, NM",
            "details": [
                "Designed and implemented user-facing software for control of custom hardware elements, integrating user input to increase usability and efficiency of user interfaces",
                "Designed, developed and integrated embedded control/DSP software",
                "Debugged and integrated multiple interconnected software and hardware elements to increase uptime, reliability and performance of a complex system",
                "Received Invertix 2008 Eagle Award for Innovation in recognition of work that contributed to the success of a critical project",
                "Assist with bench debug of RF synthesizers and receivers",
                "Evaluated capabilities and technologies before making purchasing and design recommendations for system hardware",
            ]
        },

        {
            "title": "Embedded Systems Engineering Intern",
            "org": "Applied Technology Associates",
            "org_url": "http://www.aptec.com/",
            "date": "May -- August 2007",
            "location": "Albuquerque, NM",
            "details": [
                "Developed calibration and measurement software for embedded application",
                "Performed bench integration of custom FPGA/DSP software with custom measurement hardware",
                "Developed and tested software and hardware for a variety of measurement and sensing applications",
                "Worked with other engineers to design and implement software to run on concurrently developed hardware",
            ]
        },

        {
            "title": "Research Associate",
            "org": "New Mexico Tech Institute for Complex Additive Systems Analysis",
            "org_url": "http://www.icasa.nmt.edu/",
            "date": "May 2006 -- January 2007",
            "location": "Socorro, NM",
            "details": [
                "Performed analysis on complex networks to discover significant relationships and identify key features",
                "Implemented graph/network analysis tools and metrics",
                "Developed user interfaces for data mining tools using C/C++, Java, PHP and Perl"
            ]
        },

        {
            "title": "Resident Assistant",
            "org": "New Mexico Tech Residential Life",
            "org_url": "https://www.nmt.edu/reslife/",
            "date": "August 2004 - May 2006",
            "location": "Socorro, NM",
            "details": [
                "Organized activities and programs to build and maintain a sense of community",
                "Enforced residence hall regulations for approximately 25 students"
            ]
        },

        {
            "title": "Computer Support Associate",
            "org": "New Mexico Tech Computer Center",
            "org_url": "http://infohost.nmt.edu/tcc/",
            "date": "May - August 2005",
            "location": "Socorro, NM",
            "details": [
                "Upgraded, configured, and maintained a 128-processor cluster",
                "Maintained approximately 300 networked Windows/Linux workstations",
                "Made recommendations for upgrades and new hardware for all systems"
            ]
        },

        {
            "title": "Conference Resident Assistant",
            "org": "New Mexico Tech Conference Services",
            "org_url": "http://externalweb.nmt.edu/conferences/",
            "date": "Summer 2004, Summer 2005",
            "location": "Socorro, NM",
            "details": [
                "Represented New Mexico Tech while meeting the needs of conference attendees using New Mexico Tech facilities",
            ]
        },

        {
            "title": "User Consultant",
            "org": "New Mexico Tech Technical Communications Lab",
            "org_url": "http://infohost.nmt.edu/~tc/resources/tclab.html",
            "date": "2004-2005",
            "location": "Socorro, NM",
            "details": [
                "Assist users with installation and operation of Macromedia, Adobe and Microsoft software",
                "Responsible for opening / closing of a computer lab"
            ]
        },

        {
            "title": "Independent Computer Consultant",
            "org": "",
            "org_url": "",
            "date": "May 2001 -- August 2003",
            "location": "Crane, TX",
            "details": [
                "Installed and repaired personal computers and networks in homes and businesses",
                "Diagnosed and repaired software and hardware problems on a variety of operating systems"
            ]
        },
        {
            "title": "Summer Maintenance/Technology Staff",
            "org": "Crane Independent School District",
            "org_url": "https://craneisd.com",
            "date": "May 2003 -- August 2003",
            "location": "Crane, TX",
            "details": [
                "Maintained and improved school buildings",
            ]
        },
        {
            "title": "Summer Technology Staff",
            "org": "Crane Independent School District",
            "org_url": "https://craneisd.com",
            "date": "May 2002 -- August 2002",
            "location": "Crane, TX",
            "details": [
                "Maintained teacher/student workstations",
                "Hardware troubleshooting, network hardware installation, and support of teachers upon return to school"
            ]
        },
    ],
    "programming_skills": [
        {"name": "Languages", "content": "C/C++, Objective-C, Java, PHP, Python, SQL, various assembly languages"},
        {"name": "APIs/libraries", "content": "STL, SC++L, OpenMP, OpenAL, Win32, JFC"},
        {"name": "UI design", "content": "Win32, Swing/AWT, Cocoa, and National Instruments Labwindows/CVI Scientific computation/simulation: OpenMP API, MATLAB, Octave, Numpy/Scipy"},
        {"name": "Web design", "content": "HTML, CSS, Javascript, PHP, SQL"},
        {"name": "Compiler design", "content": "scanning, parsing, optimization, instruction selection, and code emission stages"},
        {"name": "Parallel processing", "content": "Win32, OpenMP, and pthreads libraries on Windows and POSIX platforms "},
        {"name": "Development target OS", "content": "Linux, Mac OS X, Windows, embedded"},
    ],
    "engineering_skills": [
        {"name": "Microcontroller/embedded systems", "content": "Motorola HCS12, TI TMS320 DSPs in C / C++ / assembly languages"},
        {"name": "DSP", "content": "Digital filtering, signal detection, control algorithms, radar ranging, RF beamsteering using C, C++, and MATLAB on embedded and PC platforms"},
        {"name": "Lab test equipment", "content": "Oscilloscopes, function generators, signal generators, spectrum analyzers, RF network analyzers"},
        {"name": "FPGA", "content": "VHDL design using Xilinx ISE/EDK and Altera Quartus II targetting MAX7000, Spartan 3 and Virtex 4 devices"},
        {"name": "Circuit design", "content": "design, simulation and board layout using Protel/Altium DXP"},
        {"name": "Microcomputer interfacing", "content": "design and implement FPGA firmware to interface with expansion busses, including PC104/ISA, TI TMS320 DSP EMIF, and Motorola HC12"},
        {"name": "RF", "content": "VHF/UHF transmitter and receiver systems; phased arrays, RADAR, MASINT sensors"},
    ], 

    "memberships": [
        {"name": "Active security clearance", "detail": "details available on request", "org": "US Department of Defense", "org_url": ""},
        {"name": "Certified Engineer Intern", "detail": "#6693", "org": "New Mexico Board of Licensure for Professional Engineers and Surveyors", "org_url": "http://www.sblpes.state.nm.us/"},
        {"name": "Tourism Forecasting Algorithm competition", "detail": "first place", "org": "Kaggle", "org_url": "https://kaggle.com"},
        {"name": "Invertix Eagle Award for Innovation", "detail": "2008", "org": "Invertix Corporation", "org_url": "http://www.invertix.com/"},
        {"name": "Licensed Paraglider Pilot", "detail": "P2 rating", "org": "United States Hang Gliding and Paragliding Association", "org_url": ""},
        {"name": "Scuba Diver", "detail": "Rescue diver", "org": "PADI", "org_url": "http://www.padi.com/"},
        {"name": "Amateur Radio Operator", "detail": "Extra Class AE5VD", "org": "US Federal Communications Commision", "org_url": "http://wireless2.fcc.gov/UlsApp/UlsSearch/license.jsp?licKey=3247080"},
    ]
}


with open('resume.html', 'r') as f:
    contents = f.read()

template = jinja2.Template(contents)
filled_template = template.render(data=data)

with open('output.html', 'w') as f:
    f.write(filled_template)
