function z = fitnessMIT_without_P_max_117point(POP)

for iter =1:3000
chromosome = POP(iter,:);
%    our chromosom design consists of coefficent, t, s, p
error = zeros(1,117);

termLength =30;
act_index=1;
approximator =zeros(1,117);
app_index =1;
size_chromosome = size(chromosome,2);

POP_index =1;

size_decimalChromosome = (size(chromosome,2) / termLength) * 3;
decimalChromosome = zeros(1, size_decimalChromosome);


density_output = zeros(1,117);

density_output = [1002.405 1000.730 998.402 995.440  991.861  987.683  982.924  977.602  971.734  1009.929  1008.192  1005.810  1002.804  999.190  994.989  990.217  984.894  979.039  1017.516  1015.707  1013.263  1010.205  1006.552  1002.321  997.533  992.207  986.361  1025.166  1023.275  1020.761  1017.644  1013.945  1009.681  1004.873  999.539  993.699  1032.879  1030.896  1028.303  1025.121  1021.370  1017.068  1012.235  1006.891  1001.055  1040.656  1038.570  1035.891  1032.636  1028.827  1024.482  1019.621  1014.263  1008.428  1048.495  1046.298  1043.523  1040.189  1036.316  1031.923  1027.030  1021.655  1015.818  1056.398  1054.079  1051.200  1047.779  1043.837  1039.391  1034.462  1029.067  1023.225  1064.364  1061.913  1058.921  1055.407  1051.390  1046.887  1041.917  1036.498  1030.650  1072.393  1069.800  1066.688  1063.073  1058.975  1054.409  1049.395  1043.950  1038.091  1080.485  1077.741  1074.499  1070.777  1066.591  1061.959  1056.897  1051.421  1045.549  1088.640  1085.734  1082.355  1078.518  1074.240  1069.536  1064.421  1058.912  1053.025  1096.859  1093.781  1090.256  1086.298  1081.921  1077.140  1071.969  1066.424  1060.517    ]; 




% convert binary to decimal ( 10 bits for cofficent, 7 for temperature power , 7 for salinty power , 6 for pressure power )
m=1;
    for i=1:termLength:size(chromosome,2)
    coefficentVector = chromosome(:,i:(i+9));
    t_vector   = chromosome (:,i+10: i+19);
    s_vector      = chromosome (:,i+20:i+29);
    %p_vector      = chromosome (:,i+24:i+29);
 
    coefficentDec = bi2de(coefficentVector);
    t_dec =  bi2de(t_vector);
    s_dec =  bi2de(s_vector);
   % p_dec    = bi2de(p_vector);

    decimalChromosome(:,m)= coefficentDec;
    decimalChromosome(:,m+1)= t_dec;
    decimalChromosome(:,m+2)= s_dec;
    %decimalChromosome(:,m+3)= p_dec;
    
    m= m+3;
    end




p =0.1; % pressure , one fixed value for the pressure.
    for s=0:10:120 % salinty
        for t=0:10:80 % temperature
        
       

       for res = 1:3:size_decimalChromosome
        co_resoultion = decimalChromosome(1,res) ;  % needs to design a resolution here
        t_resoultion = decimalChromosome(1, res+1)/ 300;
        s_resoultion = decimalChromosome(1,res+2) / 300;
        %p_resoultion = ((decimalChromosome (1, res+3) - 30.0) /10.0);

      

%         approximator(1,app_index) = approximator(1,app_index) + co_resoultion * (t ^ t_resoultion ) * (s ^ s_resoultion ) * (p ^ p_resoultion );
                approximator(1,app_index) =  approximator(1,app_index) + co_resoultion  * (t ^ t_resoultion ) * (s ^ s_resoultion ) ; 

       end
   
     
  
    error(1,app_index) =abs( density_output(1,act_index) - approximator(1,app_index))/ (density_output(1,act_index)) ;
    
    act_index =act_index + 1; % to read the next value of excel file
   
     app_index =app_index +1;
        end
    
    end

    MSE = max(error);
   % display (error);
    %double (MSE);
    z(iter) = MSE;
  
   %z = MSE;
   
  %   display(z);
   %display(iter);
   
   
   
end
%end

    