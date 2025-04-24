# Computer-Vision-Based-Waste-Management-System
This project is under the Course No ECE 4102 and Title : Industrial and power electronics Sessional

The project is Supervised by  
Dr. Md. Shamim Ahsan,  
Professor,   
Electronics and Communication Engineering Discipline,   
Khulna University,  Khulna, Bangladesh.

Project by,
Sheyum Hossain,  
Electronics and Communication Engineering Discipline,  
Khulan University, Khulna  

# Project Video


https://github.com/user-attachments/assets/c0cf5edc-4e62-46cd-a17f-f155f5729e0f


# Objectives: 
• Develop a computer vision-based system capable of accurately identifying and
classifying various types of waste, including plastic, metal, wood, and others.  
• Design and implement a robust mechanism using stepper motors to open the
appropriate bin based on the identified waste type.  

• Integrate sensors within the bins to detect and monitor fill levels, providing real-time
data for waste collection scheduling and optimization.

#Problem Statement:
In contemporary urban environments, waste management poses a significant challenge due to
the exponential increase in population and consumption patterns. Conventional waste disposal
methods often lead to inefficient sorting, improper disposal, and environmental degradation.
Furthermore, manual waste segregation is labor-intensive, time-consuming, and prone to
errors, resulting in suboptimal resource utilization and increased operational costs for
municipalities and waste management agencies.  

# Introduction:
The proposed project aims to design and develop a state-of-the-art waste management system
utilizing computer vision technology. This system will revolutionize waste disposal processes
by automatically classifying different types of waste and directing them to corresponding bins
using stepper motor-controlled mechanisms. Additionally, the system will incorporate sensors
to monitor bin fill levels, ensuring timely waste collection and efficient management.  

# Methodology:
An operational prototype of the computer vision-based waste management system capable of
accurately identifying and sorting waste. Improved efficiency and effectiveness in waste
collection and management processes, reducing environmental impact and promoting
sustainability. Using this system waste collection and management will be easy since we
don’t have to manually sort the wastages after being dumped in the dustbin.  

Data Collection:
For sorting and classification purposes, data collection focused on three main classes: Plastic,
Metal, and Battery. To ensure diversity and representation, each class was sampled from two
sources: 50% of the data was collected using a camera module, while the remaining 50% was
obtained from the Trash Net dataset.  
Class Distribution:  

1. Plastic:
  - Total Samples:341 images
  - Data Collection Method: 50% camera module, 50% Trash Net dataset
2. Metal:
- Total Samples: 251 images
- Data Collection Method: 50% camera module, 50% Trash Net dataset
- 
3. Battery:
- Total Samples: 285 images
- Data Collection Method:50% camera module, 50% Trash Net dataset
- 
# Algorithm Design: In the classification process, OpenCV was employed as the primary
machine learning algorithm. The training parameters were configured with a learning rate of
0.001, and each batch size was set to 16.  
![image](https://github.com/user-attachments/assets/5d8ff93b-a9f8-4d8d-ac60-252cbc3af2fd)
Fig: Accuracy for Each Class  

From the Confusion we can visualize the True and Predicted Classes  
![image](https://github.com/user-attachments/assets/a78cda95-f540-4d06-a6b3-423e4ef6cd89)

Figure: Confusion Matrix  

The Algorithm achieved Accuracy of 96.85% for classifying.  
![image](https://github.com/user-attachments/assets/dfc0b364-60d2-44b9-bfb0-8be5f73faa24)

Figure: Epochs vs Accuracy  
![image](https://github.com/user-attachments/assets/6dfc909f-d18e-4fe8-bc1a-ccee1ad12ac9)

Figure: Loss Per Epoch  
# Project Figure
![image](https://github.com/user-attachments/assets/cc55b5da-b984-46bc-aa54-bf3b14671fe1)

# Conclusion:
The computer vision-based waste management system represents a significant advancement in
waste collection and recycling technologies. By automating waste sorting and bin management
processes, the system aims to optimize resource utilization and promote environmental
sustainability. With careful planning, execution, and collaboration, the project has the potential
to make a meaningful impact on waste management practices in urban and commercial settings.
