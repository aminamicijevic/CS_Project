set1_questions = [
    # Lecture 1.1: Concepts of Medical Image Post-processing (Alain Lalande)
    {
        "set_id": "Concepts of Medical Image Post-processing",
        "question": "How can we classify medical imaging techniques using electromagnetic radiation?",
        "choices": ["Only as ionizing", "Only as non-ionizing", "Ionizing and non-ionizing", "Only as tomographic"],
        "answer": "Ionizing and non-ionizing"
    },
    {
        "set_id": "Concepts of Medical Image Post-processing",
        "question": "Which medical imaging technique uses radiation that passes through the body?",
        "choices": ["Scintigraphy", "Ultrasound", "CT scanner", "MRI"],
        "answer": "CT scanner"
    },
    {
        "set_id": "Concepts of Medical Image Post-processing",
        "question": "What characterizes planar imaging in medical radiology?",
        "choices": ["Three-dimensional representation of structures", "Perspective projection", "Detection of objects regardless of surrounding tissues", "Loss of contrast and lack of depth information"],
        "answer": "Perspective projection"
    },
    {
        "set_id": "Concepts of Medical Image Post-processing",
        "question": "How can 'Partial Volume Effect (PVE)' be defined in tomographic imaging?",
        "choices": ["Loss of part of the image during compression", "Loss of information due to multiple tissue types in one voxel", "Appearance of artifacts in the image", "Visual noise in medical images"],
        "answer": "Loss of information due to multiple tissue types in one voxel"
    },
    {
        "set_id": "Concepts of Medical Image Post-processing",
        "question": "Which method of segmentation quality assessment uses an edge-based approach?",
        "choices": ["Visual evaluation", "Supervised segmentation evaluation", "Unsupervised segmentation evaluation", "Longitudinal analysis"],
        "answer": "Longitudinal analysis"
    },
    {
        "set_id": "Concepts of Medical Image Post-processing",
        "question": "In the context of medical image segmentation, what is the primary advantage of deep learning approaches?",
        "choices": ["Require a small dataset for training", "Limited to specific diseases and imaging techniques", "Provide excellent results in less than 50% of cases", "Completely automatic and outperform other methods in more than 95% of cases"],
        "answer": "Completely automatic and outperform other methods in more than 95% of cases"
    },
    {
        "set_id": "Concepts of Medical Image Post-processing",
        "question": "How is the Degree of Automation characterized in medical image segmentation?",
        "choices": ["Ideally completely automatic but generally semi-automatic", "Completely manual", "Limited to specific diseases", "Requires expertise for the training phase"],
        "answer": "Ideally completely automatic but generally semi-automatic"
    },
    {
        "set_id": "Concepts of Medical Image Post-processing",
        "question": "What is the primary purpose of medical image compression?",
        "choices": ["To increase file size", "To enhance image quality", "Efficient data transmission and storage", "To introduce visual artifacts intentionally"],
        "answer": "Efficient data transmission and storage"
    },
    {
        "set_id": "Concepts of Medical Image Post-processing",
        "question": "What is the significance of Longitudinal Analysis in medical imaging?",
        "choices": ["Detection of visual artifacts", "Real-time tele-consultation", "Detection and quantification of progressive disease over time", "Compression of medical images"],
        "answer": "Detection and quantification of progressive disease over time"
    },
    {
        "set_id": "Concepts of Medical Image Post-processing",
        "question": "What is the primary difference between imaging by transmission and imaging by emission in medical imaging?",
        "choices": [
            "Transmission uses X-rays, while emission uses magnetic fields",
            "Transmission uses radiation that passes through the body, while emission uses radiation emitted from within the body",
            "Imaging by transmission provides three-dimensional images, while imaging by emission provides two-dimensional images",
            "Imaging by emission is faster than imaging by transmission"
        ],
        "answer": "Transmission uses radiation that passes through the body, while emission uses radiation emitted from within the body"
    },
    {
        "set_id": "Concepts of Medical Image Post-processing",
        "question": "Which non-ionizing technique uses mechanic waves for imaging?",
        "choices": [
            "Computed Tomography (CT)",
            "Magnetic Resonance Imaging (MRI)",
            "Ultrasound imaging",
            "Scintigraphy"
        ],
        "answer": "Ultrasound imaging"
    },
    {
        "set_id": "Concepts of Medical Image Post-processing",
        "question": "What is the primary purpose of Planar Imaging in conventional radiology?",
        "choices": [
            "To provide three-dimensional images",
            "To map physical points into image space using perspective projection",
            "To eliminate visual noise in medical images",
            "To detect and classify objects without considering over- and underlying tissue"
        ],
        "answer": "To map physical points into image space using perspective projection"
    },
    {
        "set_id": "Concepts of Medical Image Post-processing",
        "question": "What does the term 'Principal slice orientations' refer to in medical imaging?",
        "choices": [
            "The thickness of the imaging slices",
            "Different imaging modalities",
            "Specific orientations for displaying images, such as axial, sagittal, and coronal",
            "The degree of automation in medical image segmentation"
        ],
        "answer": "Specific orientations for displaying images, such as axial, sagittal, and coronal"
    },
]

set2_questions = [
    # Lecture 1.2: The DICOM Format (Alain Lalande)
    {
        "set_id": "The DICOM Format",
        "question": "Why is anonymization of medical images performed?",
        "choices": ["To increase file size", "For promoting diagnosis", "Replacement or removal of DICOM attributes revealing personal information", "To decrease the number of optional tags in DICOM format"],
        "answer": "Replacement or removal of DICOM attributes revealing personal information"
    },
    {
        "set_id": "The DICOM Format",
        "question": "Which of the following is a drawback of the DICOM IOD (Information Object Definition)?",
        "choices": ["Small file sizes", "Strict checking of tags", "Too few optional tags", "Possible inconsistency during data recording"],
        "answer": "Possible inconsistency during data recording"
    },
    {
        "set_id": "The DICOM Format",
        "question": "What does DICOM stand for?",
        "choices": [
            "Digital Imaging and Communications in Medicine",
            "Diagnostic Imaging Communication Object Model",
            "Dynamic Image Compression and Output Module",
            "Direct Information Control for Online Medicine"
        ],
        "answer": "Digital Imaging and Communications in Medicine"
    },
    {
        "set_id": "The DICOM Format",
        "question": "What is the role of the DICOM header in a DICOM file?",
        "choices": [
            "Contains patient information",
            "Stores the actual image data",
            "Records technical information and patient data",
            "Provides compression for the image"
        ],
        "answer": "Records technical information and patient data"
    },
    {
        "set_id": "The DICOM Format",
        "question": "Which field in DICOM defines the length of the information in a data element?",
        "choices": [
            "Value Multiplicity (VM)",
            "Value Representation (VR)",
            "Tag of the DICOM dictionary",
            "Length of info"
        ],
        "answer": "Length of info"
    },
    {
        "set_id": "The DICOM Format",
        "question": "What is the significance of Value Multiplicity (VM) in DICOM?",
        "choices": [
            "It specifies the number of values that can be encoded in the value field",
            "It determines the volume of the segmented region",
            "It indicates the compression ratio for medical images",
            "It defines the type of data element"
        ],
        "answer": "It specifies the number of values that can be encoded in the value field"
    },
    {
        "set_id": "The DICOM Format",
        "question": "What is the role of Value Representation (VR) in DICOM?",
        "choices": ["It determines the value of pixels in an image", "It specifies the type of data and its format", "It measures the volume of a segmented region", "It defines the length of the DICOM header"],
        "answer": "It specifies the type of data and its format"
    },
    {
        "set_id": "The DICOM Format",
        "question": "Which type of data element in DICOM is considered Optional?",
        "choices": ["Type 1", "Type 1C", "Type 2", "Type 3"],
        "answer": "Type 3"
    },
    {
        "set_id": "The DICOM Format",
        "question": "In DICOM, what does Value Multiplicity (VM) specify?",
        "choices": ["The number of values that can be encoded in the value field", "The volume of medical images", "The type of data element", "The compression ratio for medical images"],
        "answer": "The number of values that can be encoded in the value field"
    },
    {
        "set_id": "The DICOM Format",
        "question": "What is the official compression method under DICOM?",
        "choices": ["JPEG", "PNG", "JPEG 2000", "GIF"],
        "answer": "JPEG 2000"
    },
    {
        "set_id": "The DICOM Format",
        "question": "What is DICOM?",
        "choices": ["Method for compressing medical images", "Standard format for medical images and communication between devices", "Technique for medical image post-processing", "Method for eliminating visual artifacts"],
        "answer": "Standard format for medical images and communication between devices"
    },
    {
        "set_id": "The DICOM Format",
        "question": "How is DICOM structured in terms of data?",
        "choices": ["Data is organized into two separate files", "All data is contained in one part called 'Data'", "Each data has a unique tag and consists of 8 bytes", "Data is stored in the form of free text"],
        "answer": "Each data has a unique tag and consists of 8 bytes"
    },
    {
        "set_id": "The DICOM Format",
        "question": "What is a characteristic of JPEG 2000 in the context of DICOM?",
        "choices": ["Lossy compression method", "Official lossy compression method under DICOM", "Official lossless compression method under DICOM", "Does not support compression of medical images"],
        "answer": "Official lossless compression method under DICOM"
    },
]

set3_questions = [
    # Lecture 2: Introduction to Nuclear Medicine (Alexandre Cochet)
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "What is the primary signal source in nuclear medicine imaging?",
        "choices": ["Electromagnetic radiation", "Radioactivity", "Magnetic fields", "Ultrasound waves"],
        "answer": "Radioactivity"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "How is a radiotracer administered in nuclear medicine?",
        "choices": ["Orally", "Inhaled", "Intravenously", "Topically"],
        "answer": "Intravenously"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "What determines the name of a nuclide in nuclear medicine?",
        "choices": ["Atomic number (Z)", "Mass number", "Half-life", "Radioactive constant (λ)"],
        "answer": "Atomic number (Z)"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "What is the primary difference between X-rays and gamma rays?",
        "choices": [
            "X-rays come from the nucleus, while gamma rays are produced by electronic capture",
            "Gamma rays have lower energy than X-rays",
            "X-rays are used for therapy, while gamma rays are used for diagnostics",
            "X-rays are produced by positron emission, while gamma rays are produced by electron capture"
        ],
        "answer": "X-rays come from the nucleus, while gamma rays are produced by electronic capture"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "What is the international unit for measuring radioactivity?",
        "choices": ["Curie (Ci)", "Becquerel (Bq)", "Gray (Gy)", "Sievert (Sv)"],
        "answer": "Becquerel (Bq)"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "Which isotope is commonly used in SPECT imaging?",
        "choices": ["18F", "68Ga", "99mTc", "131I"],
        "answer": "99mTc"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "What is the primary characteristic of a good radiotracer?",
        "choices": [
            "High atomic number",
            "Biological behavior different from the substance or function to be studied",
            "Long half-life",
            "High mass number"
        ],
        "answer": "Biological behavior different from the substance or function to be studied"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "What is the main advantage of FDG as a radiotracer?",
        "choices": [
            "Low radioactivity",
            "Short half-life",
            "High mass number",
            "Biological behavior identical to glucose"
        ],
        "answer": "Biological behavior identical to glucose"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "What is the primary mechanism of interaction between γ rays and matter in nuclear medicine imaging?",
        "choices": ["Pair production", "Compton scattering", "Photoelectric effect", "Neutrino emission"],
        "answer": "Photoelectric effect"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "Which imaging technique uses a collimator to filter incident photons?",
        "choices": ["CT scanner", "MRI", "SPECT", "PET"],
        "answer": "SPECT"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "What is the purpose of attenuation correction in nuclear medicine imaging?",
        "choices": ["To increase spatial resolution", "To improve image contrast", "To eliminate artifacts", "To correct for photon absorption within the patient"],
        "answer": "To correct for photon absorption within the patient"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "In PET imaging, how are coincident events defined?",
        "choices": ["Events occurring at the same time", "Events occurring in different detectors", "Events occurring within 1 microsecond", "Events occurring within 12 nanoseconds"],
        "answer": "Events occurring within 12 nanoseconds"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "What is the main advantage of SPECT over PET for multi-isotope studies?",
        "choices": [
            "Higher spatial resolution",
            "Ability to perform dynamic acquisitions",
            "Lower cost",
            "Possibility of using multiple isotopes simultaneously"
        ],
        "answer": "Possibility of using multiple isotopes simultaneously"
    },
{
        "set_id": "Introduction to Nuclear Medicine",
        "question": "Which nuclide is commonly used as a positron emitter in nuclear medicine?",
        "choices": ["99mTc", "68Ga", "18F", "131I"],
        "answer": "18F"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "What is the primary advantage of PET over SPECT in terms of spatial resolution?",
        "choices": [
            "PET has lower spatial resolution",
            "SPECT has lower spatial resolution",
            "Both PET and SPECT have similar spatial resolution",
            "PET has higher spatial resolution"
        ],
        "answer": "PET has higher spatial resolution"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "What does the term 'radiopharmaceutical' refer to in nuclear medicine?",
        "choices": [
            "A device used to shield radiation",
            "A pharmaceutical drug used to treat radiation exposure",
            "A compound used to visualize or treat diseases through its radioactivity",
            "A radioactive isotope used for therapeutic purposes"
        ],
        "answer": "A compound used to visualize or treat diseases through its radioactivity"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "What is the primary advantage of using a ring of detectors in PET imaging?",
        "choices": [
            "Increased sensitivity",
            "Reduced spatial resolution",
            "Decreased coincidence detection",
            "Limited field of view"
        ],
        "answer": "Increased sensitivity"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "Which interaction mechanism with matter is responsible for the loss of spatial information in Compton scattering?",
        "choices": ["Ionization", "Pair production", "Emission of electrons", "Change in direction"],
        "answer": "Change in direction"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "What is the primary unit for measuring the activity of a radioactive substance?",
        "choices": ["Curie (Ci)", "Becquerel (Bq)", "Gray (Gy)", "Sievert (Sv)"],
        "answer": "Becquerel (Bq)"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "In nuclear medicine, what does the term 'half-life' refer to?",
        "choices": [
            "Time required for the radioisotope to decay completely",
            "Time needed for the patient to eliminate the radiotracer",
            "Time it takes for the radiopharmaceutical to reach its peak activity",
            "Time between transmission and emission imaging"
        ],
        "answer": "Time required for the radioisotope to decay completely"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "Which of the following is a characteristic of a good radiotracer?",
        "choices": [
            "High mass number",
            "Long half-life",
            "Biological behavior unrelated to the targeted function",
            "Requires a large amount for imaging"
        ],
        "answer": "Biological behavior unrelated to the targeted function"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "What is the significance of the 511 keV gamma photons in PET imaging?",
        "choices": [
            "They provide information on tissue composition",
            "They are used for therapeutic purposes",
            "They indicate the presence of positrons",
            "They are emitted during positron-electron annihilation and used for imaging"
        ],
        "answer": "They are emitted during positron-electron annihilation and used for imaging"
    },
    {
        "set_id": "Introduction to Nuclear Medicine",
        "question": "What is the primary purpose of a collimator in a gamma camera for SPECT imaging?",
        "choices": [
            "To increase spatial resolution",
            "To filter incident photons",
            "To eliminate radioactivity",
            "To produce gamma rays"
        ],
        "answer": "To filter incident photons"
    },
]

set4_questions = [
    # Lecture 3: Some Necessary Knowledge in Medicine (Various topics)
    {
        "set_id": "Some Necessary Knowledge in Medicine",
        "question": "What is the main purpose of anatomical knowledge in medicine?",
        "choices": [
            "To increase the complexity of medical terminology",
            "To impress patients with medical jargon",
            "To provide a foundation for understanding the structure and function of the human body",
            "To memorize the names of various body parts"
        ],
        "answer": "To provide a foundation for understanding the structure and function of the human body"
    },
    {
        "set_id": "Some Necessary Knowledge in Medicine",
        "question": "Which imaging technique is best suited for providing anatomical clues about the localization, size, and shape of a structure?",
        "choices": ["PET", "Molecular imaging", "Physiological imaging", "Morphological imaging"],
        "answer": "Morphological imaging"
    },
    {
        "set_id": "Some Necessary Knowledge in Medicine",
        "question": "What is the main purpose of physiological imaging in medicine?",
        "choices": [
            "To visualize the anatomy of internal organs",
            "To detect and quantify progressive diseases over time",
            "To provide information on localized physiological functions",
            "To eliminate visual noise in medical images"
        ],
        "answer": "To provide information on localized physiological functions"
    },
    {
        "set_id": "Some Necessary Knowledge in Medicine",
        "question": "What is the term for the study of functions of living organisms and their parts?",
        "choices": ["Anatomy", "Pathology", "Physiology", "Radiology"],
        "answer": "Physiology"
    },
    {
        "set_id": "Some Necessary Knowledge in Medicine",
        "question": "In cancer, what is the term for the time when blood vessels grow to accompany tumor growth?",
        "choices": ["Angiogenic switch", "Metastatic phase", "Invasive stage", "Apoptotic stage"],
        "answer": "Angiogenic switch"
    },
    {
        "set_id": "Some Necessary Knowledge in Medicine",
        "question": "What is the primary purpose of contrast agents in medical imaging?",
        "choices": [
            "To enhance the color of medical images",
            "To increase the spatial resolution of images",
            "To simulate abnormalities in digitized radiographs",
            "To provide localized molecular/physiological information"
        ],
        "answer": "To provide localized molecular/physiological information"
    },
    {
        "set_id": "Some Necessary Knowledge in Medicine",
        "question": "What is the main purpose of attenuation correction in medical imaging?",
        "choices": ["To improve image contrast", "To eliminate artifacts", "To increase spatial resolution", "To correct for photon absorption within the patient"],
        "answer": "To correct for photon absorption within the patient"
    },
    {
        "set_id": "Some Necessary Knowledge in Medicine",
        "question": "How is sensitivity (Se) defined in the context of medical testing?",
        "choices": ["Number of true positive tests / Number of non-diseased subjects", "Number of true positive tests / Number of diseased subjects", "Number of true negative tests / Number of negative tests", "Number of diseased subjects / Total number of studied subjects"],
        "answer": "Number of true positive tests / Number of diseased subjects"
    },
    {
        "set_id": "Some Necessary Knowledge in Medicine",
        "question": "What does Positive Predictive Value (PPV) represent in medical testing?",
        "choices": ["Probability of having the disease after a positive test", "Probability of having the disease after a negative test", "Overall survival", "Progression-free survival"],
        "answer": "Probability of having the disease after a positive test"
    },
    {
        "set_id": "Some Necessary Knowledge in Medicine",
        "question": "What is the primary positive aspect of Artificial Intelligence (AI) in medicine?",
        "choices": [
            "Increased patient safety",
            "Improved privacy and data protection",
            "Enhanced human values",
            "Time-saving and exploration of large amounts of information"
        ],
        "answer": "Time-saving and exploration of large amounts of information"
    },
    {
        "set_id": "Some Necessary Knowledge in Medicine",
        "question": "What is a potential issue associated with the application of Artificial Intelligence (AI) in medicine?",
        "choices": ["Improved transparency and explainability", "Avoidance of bias", "Privacy concerns and data protection", "Smooth integration with existing medical practices"],
        "answer": "Privacy concerns and data protection"
    },
    {
        "set_id": "Some Necessary Knowledge in Medicine",
        "question": "What is the role of AI in medical education according to the lecture?",
        "choices": [
            "Replacement of doctors in providing medical advice",
            "Refocusing medical education on knowledge recall",
            "Setting up virtual patients for medical education",
            "Limited to enhancing visual perception of medical images"
        ],
        "answer": "Setting up virtual patients for medical education"
    },
]

set5_questions = [
    {
        "set_id": "Optical imaging: Bioluminescence & Fluorescence",
        "question": "What is the primary focus of preclinical imaging?",
        "choices": [
            "Studying external light sources",
            "Visualizing only anatomical structures",
            "Characterizing and measuring biological processes at the molecular and cellular levels",
            "Conducting invasive biopsies"
        ],
        "answer": "Characterizing and measuring biological processes at the molecular and cellular levels"
    },
    {
        "set_id": "Optical imaging: Bioluminescence & Fluorescence",
        "question": "What are the hallmarks of cancer, and how do they relate to molecular imaging in oncology?",
        "choices": [
            "Biological processes in normal cells",
            "Targets for biomarkers in pharmacology",
            "Complex biological processes in cancer cells",
            "Genetic variations in healthy individuals"
        ],
        "answer": "Complex biological processes in cancer cells"
    },
    {
        "set_id": "Optical imaging: Bioluminescence & Fluorescence",
        "question": "What distinguishes molecular imaging from tissue-based molecular assays, such as biopsies?",
        "choices": [
            "Invasive nature",
            "Non-invasiveness and assessment of the entire burden of a disease",
            "Studying external light sources",
            "Regional heterogeneity"
        ],
        "answer": "Non-invasiveness and assessment of the entire burden of a disease"
    },
    {
        "set_id": "Optical imaging: Bioluminescence & Fluorescence",
        "question": "What is the primary advantage of optical imaging in preclinical steps?",
        "choices": [
            "High depth of penetration in clinical settings",
            "Invasive nature for accurate measurements",
            "Efficiency in preclinical steps",
            "Limited sensitivity to biological processes"
        ],
        "answer": "Efficiency in preclinical steps"
    },
    {
        "set_id": "Optical imaging: Bioluminescence & Fluorescence",
        "question": "Describe the key principles of bioluminescence imaging and its applications.",
        "choices": [
            "Requires an excitation light, low sensitivity, and clinical translatability",
            "Utilizes luciferases, emits photons without excitation light, and has higher sensitivity",
            "Involves radioactivity and limited depth of penetration",
            "Primarily used for clinical translation"
        ],
        "answer": "Utilizes luciferases, emits photons without excitation light, and has higher sensitivity"
    },
    {
        "set_id": "Optical imaging: Bioluminescence & Fluorescence",
        "question": "What are the advantages and limitations of fluorescence imaging?",
        "choices": [
            "Unlimited depth of penetration, high sensitivity, and simplicity",
            "Limited depth of penetration, potential toxicity, and higher cost",
            "Primarily used for bioluminescence imaging",
            "No need for external light sources and low versatility"
        ],
        "answer": "Limited depth of penetration, potential toxicity, and higher cost"
    },
    {
        "set_id": "Optical imaging: Bioluminescence & Fluorescence",
        "question": "What is the window of transparency, and why is it crucial for optical imaging?",
        "choices": [
            "Region with high absorption, ideal for imaging",
            "Region with low absorption, allowing deeper imaging",
            "Invasive technique for image acquisition",
            "Primarily used for bioluminescence imaging"
        ],
        "answer": "Region with low absorption, allowing deeper imaging"
    },
    {
        "set_id": "Optical imaging: Bioluminescence & Fluorescence",
        "question": "Explain the basic process of bioluminescence and how it differs from fluorescence.",
        "choices": [
            "Requires an excitation light, involves fluorescence proteins, and has limited sensitivity",
            "Utilizes luciferases, emits photons without excitation light, and has higher sensitivity",
            "Involves radioactivity, limited depth of penetration, and clinical translatability",
            "Primarily used for clinical translation"
        ],
        "answer": "Utilizes luciferases, emits photons without excitation light, and has higher sensitivity"
    },
    {
        "set_id": "Optical imaging: Bioluminescence & Fluorescence",
        "question": "What are the major challenges in fluorescence imaging, and how can they be addressed?",
        "choices": [
            "Unlimited depth of penetration, simplicity, and low cost",
            "Limited depth of penetration, potential toxicity, and autofluorescence",
            "Primarily used for bioluminescence imaging",
            "No need for external light sources and low versatility"
        ],
        "answer": "Limited depth of penetration, potential toxicity, and autofluorescence"
    },
    {
        "set_id": "Optical imaging: Bioluminescence & Fluorescence",
        "question": "Describe the trend of 3D/Tomography in in vivo imaging systems and its advantages.",
        "choices": [
            "Primarily used for 2D classical fluorescence, lower quantifications, and depths",
            "Better than 2D classical fluorescence, better quantifications, and greater depths",
            "Involves radioactivity and limited depth of penetration",
            "Requires external light sources and high cost"
        ],
        "answer": "Better than 2D classical fluorescence, better quantifications, and greater depths"
    }
]

set6_questions = [
    {
        "set_id": "AI and Neuroscience",
        "question": "What is the primary focus of artificial intelligence (AI) as mentioned in the lesson?",
        "choices": [
            "Simulation of computer processes",
            "Replication of physiological functions",
            "Automation of mechanical tasks",
            "Mimicking human intelligence processes"
        ],
        "answer": "Mimicking human intelligence processes"
    },
    {
        "set_id": "AI and Neuroscience",
        "question": "What are the applications of AI in the health sector?",
        "choices": [
            "Automated screening of cell cultures for abnormalities",
            "Automated surgery procedures",
            "Real-time monitoring of patient emotions",
            "Automated prescription of medications"
        ],
        "answer": "Automated screening of cell cultures for abnormalities"
    },
    {
        "set_id": "AI and Neuroscience",
        "question": "How is Symbolic AI different from Machine Learning in terms of knowledge representation?",
        "choices": [
            "Symbolic AI uses explicit symbols, while Machine Learning uses implicit representations",
            "Symbolic AI is limited to visual perception, while Machine Learning covers decision-making",
            "Machine Learning uses explicit symbols, while Symbolic AI uses implicit representations",
            "Symbolic AI and Machine Learning use the same knowledge representation methods"
        ],
        "answer": "Symbolic AI uses explicit symbols, while Machine Learning uses implicit representations"
    },
    {
        "set_id": "AI and Neuroscience",
        "question": "What is the primary characteristic of Reinforcement Learning in machine learning?",
        "choices": [
            "The correct answer is provided in the network",
            "The correct answer is not present in the network, and there is no reward for the right answer",
            "The correct answer is not presented, but there is a reward or punishment for answers",
            "The correct answer is not presented, and there is no reward or punishment"
        ],
        "answer": "The correct answer is not presented, but there is a reward or punishment for answers"
    },
    {
        "set_id": "AI and Neuroscience",
        "question": "Describe the types of learning in machine learning, focusing on Supervised Learning.",
        "choices": [
            "Supervised Learning involves no feedback and no evaluation",
            "In Unsupervised Learning, the correct answer is provided in the network",
            "Supervised Learning includes feedback and evaluation with a correct answer provided in the network",
            "Reinforcement Learning involves no feedback and no evaluation"
        ],
        "answer": "Supervised Learning includes feedback and evaluation with a correct answer provided in the network"
    },
    {
        "set_id": "AI and Neuroscience",
        "question": "Explain the structure of a neuron and its basic functions.",
        "choices": [
            "Soma receives input, dendrite sends output, and axon contains the nucleus",
            "Soma sends output, dendrite contains the nucleus, and axon receives input",
            "Soma contains the nucleus, dendrite receives input, and axon sends output",
            "Soma receives input, dendrite contains the nucleus, and axon sends output"
        ],
        "answer": "Soma contains the nucleus, dendrite receives input, and axon sends output"
    },
    {
        "set_id": "AI and Neuroscience",
        "question": "What is the source of electricity in biological neurons?",
        "choices": [
            "Light absorption",
            "Chemical reactions",
            "Differential distribution of charges (ions) across the neuronal membrane",
            "Kinetic energy"
        ],
        "answer": "Differential distribution of charges (ions) across the neuronal membrane"
    },
    {
        "set_id": "AI and Neuroscience",
        "question": "Explain the effects of excitatory neurotransmitters on the postsynaptic neuron.",
        "choices": [
            "Negative response, increased firing rate",
            "Positive response, increased depolarization",
            "Negative response, decreased firing rate",
            "Positive response, decreased depolarization"
        ],
        "answer": "Positive response, increased depolarization"
    },
    {
        "set_id": "AI and Neuroscience",
        "question": "What is the role of temporal summation in neurons?",
        "choices": [
            "Occurs at low frequencies",
            "Occurs at high frequencies",
            "Occurs in the absence of stimuli",
            "Biological mechanism for weight change"
        ],
        "answer": "Occurs at high frequencies"
    },
    {
        "set_id": "AI and Neuroscience",
        "question": "Explain Hebb’s Law and its relevance to neural networks.",
        "choices": [
            "Cells that fire together are wired apart",
            "Cells that fire together wire together",
            "Cells that fire together do not influence each other",
            "Cells that fire together create feedback loops"
        ],
        "answer": "Cells that fire together wire together"
    },

]

set7_questions = [
    {
        "set_id": "Computer Aided Diagnosis for Retina Related Diseases",
        "question": "What are some common eye pathologies mentioned in the lesson?",
        "choices": [
            "Conjunctivitis and Myopia",
            "Cataract, Glaucoma, Diabetic retinopathy, Age Macula Degenerescence",
            "Astigmatism and Presbyopia",
            "Keratitis and Uveitis"
        ],
        "answer": "Cataract, Glaucoma, Diabetic retinopathy, Age Macula Degenerescence"
    },
    {
        "set_id": "Computer Aided Diagnosis for Retina Related Diseases",
        "question": "What imaging tools are used for examining the eye?",
        "choices": [
            "Stethoscope and X-ray",
            "Ophthalmoscope and Ultrasound",
            "Microscopy, Angiography, Endoscopy",
            "Blood pressure cuff and MRI"
        ],
        "answer": "Microscopy, Angiography, Endoscopy"
    },
    {
        "set_id": "Computer Aided Diagnosis for Retina Related Diseases",
        "question": "What is the solution to achieve one maximum per tissue layer in OCT?",
        "choices": [
            "Use a single narrow-band light source",
            "Use a broadband (Gaussian) light source",
            "Increase the intensity of the light source",
            "Reduce the speed of the scanning mirror"
        ],
        "answer": "Use a broadband (Gaussian) light source"
    },
    {
        "set_id": "Computer Aided Diagnosis for Retina Related Diseases",
        "question": "What is the first detectable sign of diabetic retinopathy?",
        "choices": [
            "Retinal hemorrhages",
            "Hard exudates",
            "Microaneurysms",
            "Drusens"
        ],
        "answer": "Microaneurysms"
    },
    {
        "set_id": "Computer Aided Diagnosis for Retina Related Diseases",
        "question": "How are drusens visualized in Age-related Macular Degeneration?",
        "choices": [
            "As black dots in the retina",
            "As whitish yellow deposits under the retinal pigment epithelium and neurosensory retina",
            "As red streaks in the vitreous humor",
            "As irregular patterns on the optic nerve"
        ],
        "answer": "As whitish yellow deposits under the retinal pigment epithelium and neurosensory retina"
    },
    {
        "set_id": "Computer Aided Diagnosis for Retina Related Diseases",
        "question": "What is one advantage of Eye Screening with Fundus Cameras?",
        "choices": [
            "Pupil dilation is required",
            "Requires contrast agent",
            "Highly invasive",
            "Usable by non-ophthalmologists without pupil dilation or contrast agent"
        ],
        "answer": "Usable by non-ophthalmologists without pupil dilation or contrast agent"
    },
{
        "set_id": "Computer Aided Diagnosis for Retina Related Diseases",
        "question": "What are some common eye pathologies mentioned, and briefly describe each?",
        "choices": [
            "Cataract, Glaucoma, Diabetic retinopathy, Age Macula Degenerescence",
            "Astigmatism, Myopia, Hyperopia, Presbyopia",
            "Conjunctivitis, Keratitis, Uveitis, Retinitis",
            "Floaters, Dry eye, Red eye, Retinal detachment"
        ],
        "answer": "Cataract, Glaucoma, Diabetic retinopathy, Age Macula Degenerescence"
    },
    {
        "set_id": "Computer Aided Diagnosis for Retina Related Diseases",
        "question": "What are the imaging tools mentioned for diagnosing retina-related diseases, and briefly explain one of them?",
        "choices": [
            "Microscopy, Oculometry, Endoscopy, Angiography, Fundus imaging, OCT",
            "X-ray, Ultrasound, MRI, CT scan, PET scan, Mammography",
            "Electrocardiography, Spirometry, Blood tests, Urinalysis",
            "Laparoscopy, Colonoscopy, Arthroscopy, Endoscopic retrograde cholangiopancreatography (ERCP)"
        ],
        "answer": "Microscopy, Oculometry, Endoscopy, Angiography, Fundus imaging, OCT"
    },
    {
        "set_id": "Computer Aided Diagnosis for Retina Related Diseases",
        "question": "Explain the use of Optical Coherence Tomography (OCT) in retina imaging.",
        "choices": [
            "OCT uses sound waves to create detailed images of the retina",
            "OCT uses magnetic fields to visualize retinal structures",
            "OCT uses a broadband light source and Fourier transform to create high-resolution images",
            "OCT relies on radioactive tracers for imaging"
        ],
        "answer": "OCT uses a broadband light source and Fourier transform to create high-resolution images"
    },
    {
        "set_id": "Computer Aided Diagnosis for Retina Related Diseases",
        "question": "What are the typical signs of diabetic retinopathy mentioned in the lecture?",
        "choices": [
            "Microaneurysms, Retinal hemorrhages, Hard exudates",
            "Yellow deposits, Loss of normal fovea contour, Cystic space formation",
            "Drusens, Narrowed vision, Loss of normal anatomy of the inner retina layer",
            "Loss of fovea contour, Interruption of outer retina layer, Whitish yellow deposits"
        ],
        "answer": "Microaneurysms, Retinal hemorrhages, Hard exudates"
    },
    {
        "set_id": "Computer Aided Diagnosis for Retina Related Diseases",
        "question": "How is eye screening with Fundus Cameras advantageous for non-ophthalmologists?",
        "choices": [
            "Requires pupil dilation",
            "Needs a contrast agent",
            "Involves low-quality images",
            "Does not require pupil dilation or a contrast agent"
        ],
        "answer": "Does not require pupil dilation or a contrast agent"
    },
    {
        "set_id": "Computer Aided Diagnosis for Retina Related Diseases",
        "question": "What role does Computer Aided Diagnosis (CAD) play in the health sector, specifically in the context of eye pathologies?",
        "choices": [
            "CAD is primarily used for surgical procedures",
            "CAD automates the screening of cell cultures for abnormalities",
            "CAD assists in physiological measurements during diagnosis",
            "CAD aids in automated screening, diagnosis, and decision-making for eye diseases"
        ],
        "answer": "CAD aids in automated screening, diagnosis, and decision-making for eye diseases"
    },
{
        "set_id": "AI and Neuroscience",
        "question": "Define Artificial Intelligence (AI) and provide examples of tasks it can perform.",
        "choices": [
            "AI is the study of animals' intelligence. Examples include dog training and bird mimicry",
            "AI refers to computer systems performing tasks requiring human intelligence, like visual perception and speech recognition. Examples include image recognition and language translation",
            "AI stands for Augmented Intelligence, assisting humans with everyday tasks. Examples include GPS navigation and online calendars",
            "AI is the study of ancient civilizations and their artifacts. Examples include archaeology and paleontology"
        ],
        "answer": "AI refers to computer systems performing tasks requiring human intelligence, like visual perception and speech recognition. Examples include image recognition and language translation"
    },
    {
        "set_id": "AI and Neuroscience",
        "question": "Explain the division of AI into Symbolic AI and Machine Learning. Provide examples of each.",
        "choices": [
            "Symbolic AI uses symbols to represent knowledge. Example: GPS navigation. Machine Learning uses neural networks. Example: voice recognition",
            "Symbolic AI uses neural networks for decision-making. Example: image recognition. Machine Learning uses logic and rules. Example: expert systems",
            "Symbolic AI focuses on computer vision. Example: facial recognition. Machine Learning relies on rule-based systems. Example: autonomous vehicles",
            "Symbolic AI is based on quantum computing. Example: weather prediction. Machine Learning uses decision trees. Example: credit scoring"
        ],
        "answer": "Symbolic AI uses symbols to represent knowledge. Example: GPS navigation. Machine Learning uses neural networks. Example: voice recognition"
    },
    {
        "set_id": "AI and Neuroscience",
        "question": "Explain the concept of Supervised Learning in Machine Learning. Provide an example.",
        "choices": [
            "Supervised Learning involves training a model with labeled data, where the correct answers are provided. Example: handwriting recognition",
            "Supervised Learning relies on trial and error for training. Example: autonomous robotics",
            "Supervised Learning is a self-learning process without labeled data. Example: language translation",
            "Supervised Learning doesn't involve a learning phase. Example: image classification"
        ],
        "answer": "Supervised Learning involves training a model with labeled data, where the correct answers are provided. Example: handwriting recognition"
    },
    {
        "set_id": "AI and Neuroscience",
        "question": "What is Hebb's Law, and how does it relate to neural networks?",
        "choices": [
            "Hebb's Law states that neurons fire randomly. It doesn't relate to neural networks",
            "Hebb's Law is about the role of neurotransmitters. It relates to drug development",
            "Hebb's Law states that cells that fire together wire together, reinforcing synaptic connections. It relates to associative learning in neural networks",
            "Hebb's Law deals with the anatomy of the human brain. It relates to neuroanatomy"
        ],
        "answer": "Hebb's Law states that cells that fire together wire together, reinforcing synaptic connections. It relates to associative learning in neural networks"
    },
    {
        "set_id": "AI and Neuroscience",
        "question": "Explain the concept of Corticogenesis and Axonal Guidance in neural development",
        "choices": [
            "Corticogenesis involves drug-induced sleep. Axonal Guidance is about blood circulation",
            "Corticogenesis is the study of cortical areas. Axonal Guidance is unrelated to neural development",
            "Corticogenesis and Axonal Guidance are part of brain development, involving cell proliferation, migration, and synapse formation",
            "Corticogenesis is about muscle development. Axonal Guidance relates to eye movements"
        ],
        "answer": "Corticogenesis and Axonal Guidance are part of brain development, involving cell proliferation, migration, and synapse formation"
    },
]

set8_questions = [
    {
        "set_id": "Preclinical imaging of the rodent brain",
        "question": "What are the three primary brain vesicles that emerge from the neural tube around day 28 of human CNS development?",
        "choices": [
            "Forebrain, Midbrain, and Hindbrain",
            "Telencephalon, Diencephalon, and Myelencephalon",
            "Prosencephalon, Mesencephalon, and Rhombencephalon",
            "Cerebral hemispheres, Pons, and Medulla oblongata"
        ],
        "answer": "Prosencephalon, Mesencephalon, and Rhombencephalon"
    },
    {
        "set_id": "Preclinical imaging of the rodent brain",
        "question": "What are the two main mechanisms during corticogenesis?",
        "choices": [
            "Phototropism and Gravitropism",
            "Proliferation and Neurogenesis",
            "Mitosis and Meiosis",
            "Axonogenesis and Synaptogenesis"
        ],
        "answer": "Proliferation and Neurogenesis"
    },
    {
        "set_id": "Preclinical imaging of the rodent brain",
        "question": "What is the main difference mentioned between the human and mouse brain?",
        "choices": [
            "Mouse brain has more encephalic convolutions",
            "Mouse brain has fewer encephalic convolutions",
            "Human brain is less encephalic",
            "Human brain is more tubular"
        ],
        "answer": "Mouse brain has fewer encephalic convolutions"
    },
    {
        "set_id": "Preclinical imaging of the rodent brain",
        "question": "What is the purpose of Episcopic bloc face imaging in 3D histology?",
        "choices": [
            "To create 3D models of historical landmarks",
            "To visualize serial sections in 3D without histology",
            "To study ancient artifacts in three dimensions",
            "To perform rapid serial microscopy"
        ],
        "answer": "To visualize serial sections in 3D without histology"
    },
    {
        "set_id": "Preclinical imaging of the rodent brain",
        "question": "What is the main advantage of MRI over other imaging techniques?",
        "choices": [
            "Low cost",
            "Superior soft tissue contrast for structural segmentation",
            "High resolution below 10 μm",
            "No limitations on spatial resolution"
        ],
        "answer": "Superior soft tissue contrast for structural segmentation"
    },
    {
        "set_id": "Preclinical imaging of the rodent brain",
        "question": "What does Diffusion MRI measure, and what information does it provide about the tissue?",
        "choices": [
            "Measures blood flow; Provides information about tissue density",
            "Measures tissue deformation; Provides information about tissue elasticity",
            "Measures water molecule diffusion; Provides information about tissue density and cell membrane integrity",
            "Measures electrical conductivity; Provides information about tissue conductivity"
        ],
        "answer": "Measures water molecule diffusion; Provides information about tissue density and cell membrane integrity"
    },
    {
        "set_id": "Preclinical imaging of the rodent brain",
        "question": "What is Geometric morphometrics, and how is it applied in biological studies?",
        "choices": [
            "A technique for DNA sequencing; Applied in genetic diagnosis",
            "A technique for measuring brain electrical activity; Applied in neuroscience",
            "A technique for integrating size and shape in biological studies; Applied in morphometric analysis",
            "A technique for studying fossilized organisms; Applied in paleontology"
        ],
        "answer": "A technique for integrating size and shape in biological studies; Applied in morphometric analysis"
    },
{
        "set_id": "Preclinical imaging of the rodent brain",
        "question": "What are the three cell layers formed during embryonic disc formation, and what does the ectoderm develop into?",
        "choices": [
            "Endoderm, Mesoderm, Ectoderm; Develops into neural plate",
            "Ectoderm, Mesoderm, Endoderm; Develops into neural crest",
            "Endoderm, Ectoderm, Mesoderm; Develops into somites",
            "Mesoderm, Ectoderm, Endoderm; Develops into neural tube"
        ],
        "answer": "Endoderm, Mesoderm, Ectoderm; Develops into neural plate"
    },
    {
        "set_id": "Preclinical imaging of the rodent brain",
        "question": "What is the significance of the dorsal or where stream in vision processing?",
        "choices": [
            "Associated with spatial awareness and guidance of actions",
            "Responsible for color vision",
            "Primarily involved in low-light vision",
            "Responsible for peripheral vision"
        ],
        "answer": "Associated with spatial awareness and guidance of actions"
    },
    {
        "set_id": "Preclinical imaging of the rodent brain",
        "question": "Explain the concept of synaptic pruning and its role in neural development",
        "choices": [
            "Synaptic pruning involves the formation of new synapses during neural development",
            "Synaptic pruning is the elimination of unused or unnecessary synapses",
            "Synaptic pruning only occurs in the spinal cord",
            "Synaptic pruning is not relevant to neural development"
        ],
        "answer": "Synaptic pruning is the elimination of unused or unnecessary synapses"
    },
    {
        "set_id": "Preclinical imaging of the rodent brain",
        "question": "What is the primary limitation mentioned for MRI in preclinical imaging of the rodent brain?",
        "choices": [
            "Low spatial resolution",
            "Limited soft tissue contrast",
            "High cost",
            "Inability to visualize blood flow"
        ],
        "answer": "Low spatial resolution"
    },
    {
        "set_id": "Preclinical imaging of the rodent brain",
        "question": "In diffusion MRI, what does diffusion anisotropy reflect?",
        "choices": [
            "Density of water molecules",
            "Directionality of water diffusion",
            "Inhomogeneities in the magnetic field",
            "Blood or cerebrospinal fluid movement"
        ],
        "answer": "Directionality of water diffusion"
    },
    {
        "set_id": "Preclinical imaging of the rodent brain",
        "question": "How does Geometric morphometrics contribute to morphometric analysis in brain research?",
        "choices": [
            "It measures brain electrical activity",
            "It quantifies brain volume",
            "It integrates size and shape for biological meaningfulness",
            "It analyzes DNA sequencing data"
        ],
        "answer": "It integrates size and shape for biological meaningfulness"
    },
]

quiz_data = (set1_questions + set2_questions + set3_questions + set4_questions + set5_questions + set6_questions
             + set7_questions + set8_questions)
