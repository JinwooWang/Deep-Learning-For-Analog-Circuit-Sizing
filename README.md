# DL-for-Analog-Sizing
This Project is a Research about the combination of Analog Circuit Sizing and Deep Learning. We aimed to generate some great 
sizings with specific performance(Adc, GBW, PM, etc.)
Here we used DNN and RNN as our model. 
## Data Generation
Using ngspice to generate certain amount of data for our two-stage Op-Amp. The testbenches are provided in this repo.
## Build Model
Using tensorflow to build our DNN and RNN(LSTM).
## Model Evaluation
Using these models to generate some test data and feed them into the simulator(ngspice). Then compare the given preformance with the simulated results.
## PS: 
for more information, just check our paper(Zhenyu Wang, Xiangzhong Luo, Zheng Gong. Application of Deep Learning in Analog Circuit Sizing. In 2018 2nd International Conference on Computer Science and Artificial Intelligence)(https://dl.acm.org/citation.cfm?id=3297156)
