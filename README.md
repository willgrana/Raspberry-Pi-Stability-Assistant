# Raspberry-Pi-Stability-Assistant
Flask web app displaying data such as CPU core voltage and clock for stress and stability testing a Raspberry Pi.

Final Project Proposal: Cooling the Pi


#Table of Contents:

	Introduction (P. 4)
	Definitions, Acronyms, and Abbreviations (P. 5)
	Project Detail (P. 5)
	Budget (P. 6)
	Project Plan (P. 7)
	Target Market (P. 6)
	References (P. 7)


#Introduction:


Computers take energy to run. Energy in the form of electricity allows vital system components to function together to complete a task. When a computer uses this energy, some of it is lost due to heat. All components have a certain thermal limit that they must not exceed, otherwise circuitry will be damaged and this can break the component forever. We have come to combat this thermal limit on our processing power with active and passive cooling solutions, the most basic of which is simply a heatsink mounted to whichever component needs to stay cool. By adding fans to this heatsink, cycling air, we can furthermore increase the performance of this cooling. Active cooling is the process by which we apply more energy to cool something. These two cooling solutions use a heatsink as a medium to transfer heat energy into the air and out of the component, such as the CPU or GPU. However, air is actually quite a poor medium for heat transfer, with a specific heat of only 1.005  kJ/(kg×K). If we could transfer the heat to a different substance, like water, which has a much higher specific heat of 4.186  kJ/(kg×K), we could remove much more thermal energy allowing us to increase the power applied to the component, increasing its performance. Many modern computer systems do take advantage of water cooling, and this method has proven to be extremely effective. In the case of the Raspberry Pi, no cooling methods have been applied to the system at all, active or passive. Because the power draw of the ARM processor is so small, we can get away with simply letting the heat pass straight from the chip to the air. However, after you use the Pi for a while in a single sitting, you may find speeds to complete simple tasks start to take a drastic fall. Once the ARM processor hits a temperature of 82 degrees Celsius, the Pi has no choice but to limit its processing through underclocking the ARM chip and lowering the core voltage so as to not increase temperature even further, as this would permanently damage the chip. If we could come up with a way to more effectively cool the Pi, we could run at full load for extended periods of time, whilst also running at higher clock speeds and core voltage, increasing the performance of the chip. Cooler components also have longer lifespans, so by running the Pi at lower temperatures, we extend the life of its CPU and the board itself.



Definitions, Acronyms, and Abbreviations:

	Clock Speed: the speed at which the processor can execute instructions.
	Core Voltage: The amount of power that can be drawn by the CPU.
	Specific Heat: A measure of how much and how effectively thermal energy can be stored by a substance.
	Passive Cooling: a method of cooling something with no additional energy added to the system.
	Active Cooling: a method of cooling something with additional energy added to the system.
	CPU: Central Processing Unit, the chip which executes logic statements.
	ARM: Advanced RISC Machine, a family of RISC architectures for computer processors.
	RISC: Reduced instruction set computing.
	Heatsink: A device for absorbing excess heat.
	Mineral Oil: A non-conductive, fluid medium.


#Project Detail


I plan to improve the thermals of the Raspberry Pi by means of active cooling so that the ARM chip may be overclocked to yield increased performance, while still avoiding thermal throttling. I plan on doing this by means of mineral oil cooling. Because mineral oil is completely nonconductive, this means that components that are very sensitive to electrical input can be totally submerged in the oil. Essentially, instead of exhausting thermal energy into the air, I will exhaust the thermal energy into the mineral oil. While mineral oil does not come close to water’s specific heat, it is still much better than air, with a specific heat of 1.67  kJ/(kg×K). I will design a case with a fan to cycle the mineral oil through a radiator, which will help to furthermore release thermal energy from the system. Through these thermal enhancements, I will be able to increase the computing power of the Pi by increasing the clock rate of the ARM chip, whilst extending the life of the Pi at the same time.

#Budget:

Part	Cost
1 Gallon Mineral Oil	$17.00
Fan	$7.99
Case	Free
Labor	Free
Total	$24.99


#Project Plan:
 

#Target Market:


The target market for this prototype will be manufactures of low power draw systems such as Raspberry Pis and cell phones, showing them the capabilities of mineral oil cooling.


#References:


J. M. Shah, R. Eiland, A. Siddarth and D. Agonafer, "Effects of mineral oil immersion cooling on IT equipment reliability and reliability enhancements to data center operations," 2016 15th IEEE Intersociety Conference on Thermal and Thermomechanical Phenomena in Electronic Systems (ITherm), Las Vegas, NV, 2016, pp. 316-325.

https://ieeexplore.ieee.org/abstract/document/7517566

https://patents.google.com/patent/US7403392B2/en




















#Projected vs Actual Time and Cost Analysis

Over the few weeks of working on my project, I put in roughly five hours a week planning and building my prototype. I believe my success in pacing my work in project yielded a solid final product and great data on different cooling solutions for the Pi. As far as cost, I ended up using a Tupperware container which I already had as the case so this was free, and the fan was slightly more expensive than I anticipated. My end cost was less than my projected cost. Since I did not have any means of fabrication in my home while quarantined, I was unable to build a radiator to cool the mineral oil, but since the heat output of the Pi is so low, this made no difference in the end results.




#Final Reflection and Data

For my project, I successfully cooled my Raspberry Pi with mineral oil. I ran both a temperature throttling benchmark, as well as a processing power benchmark to measure the gains from each clock speed and cooling configuration. I built a flask app which shows CPU temperature, core clock, core voltage, CPU utilization, ram utilization, and ambient temperature in real time, updating 5 times a second so that I could accurately monitor my Pi remotely while the tests were running. Below is the data that I have gathered from my tests.



 

First, let’s look at some benchmark data. For the benchmark, I used a program called Sysbench to check for prime numbers up to 20,000. The above graph shows the time till completion for each clock speed and voltage setting with different cooling methods. Surprisingly, the engineers who made the Pi 4 have built in a decent amount of cooling capabilities right out of the box, as my Pi was able to remain thermally stable with a 200mHz boost over stock, allowing for a 11.78% increase in processing power. With a fan installed, I was able to reach a 550mHz boost over stock, yielding a 26.77& increase in processing power. Using mineral oil cooling, I reached a firmware limited 2147mHz, a 647mHz boost over stock, yielding a 30.17% increase in processing power. With adequate cooling, the Pi proved to pack quite a punch for a $40 computer with its Broadcom processor.

 


Now, let’s look at some temperature data. For this test, I used a program called cpuBurn-a53. This program loads the processor with tasks designed to produce the most heat. All runs started at a CPU temperature of 40C, with an ambient temperature of 21C. The stock Pi at 1500mHz took roughly 12 minutes to thermal throttle, a respectable baseline run. Overclocking the Pi to 1700mHz whilst still using no cooling produced a time till thermal throttle of roughly 3:30s, which is about 3.5 times faster than stock. Adding a fan to the Pi at this same frequency yielded a time till thermal throttle of over 36 minutes. By adding just a fan, I nearly increased the thermal performance of the Pi buy 10 times, a remarkable figure showing the benefits of active cooling. It seemed that 1700mHz is a real sweet spot for my chip as the following increases to the core clock caused time to thermal throttle to rapidly decrease, as seen in the above graph. When it was time to cool the Pi with a mineral oil bath, the results were astounding. Running the Pi in oil with both a 2050mHz clock and a 2147mHz clock, the test was able to run for over two hours with no thermal throttling, with both clocks stabilizing at roughly 70 degrees Celsius. This is a remarkable outcome: you could run the Pi with 30% more processing power almost indefinitely with mineral oil cooling, showing the effectiveness of this approach to cooling.


Conclusion

Through this project, I have found that active cooling is extremely effective, making an especially large difference on small systems like the Raspberry Pi. If you can combine active cooling with a better heat transfer medium than air such as mineral oil, the results are astounding: 30% more processing power whilst maintaining cooler temperatures than a stock system, making for a longer lasting, more powerful computer. I believe that one day, active cooling will have a place in small computer systems like smart phones as processors become more powerful and thermal technologies fail to keep pace with the heat output of these new powerful processors. It is also important to note that note all chips are identical, that is that there is a bit of a “Silicon Lottery”, meaning some chips may be capable of higher core clocks and lower temperatures than others. I believe that I may have gotten lucky with my Broadcom chip and its overclocking potential. I can now say that I have one of the world’s fastest, coolest running Raspberry Pis!

Project Video

https://www.youtube.com/watch?v=ea0SEwc-onI


