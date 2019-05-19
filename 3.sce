function [H]=generateHadamardMatrix(codeSize) 
N=2;
H=[1 1 ; 1 -1];
H1=[1];
if(codeSize==1)
 H = H1
end
if (bitand(codeSize,codeSize-1)==0 && codeSize ~= 1)
    while(N~=codeSize)
           N=N*2;
           H=repmat(H,[2,2]);
           [m,n]=size(H);
          for i=m/2+1:m,
              for j=n/2+1:n,
                    H(i,j)= -H(i,j);
             end
         end
    end
else
disp('INVALID CODE SIZE:The code size must be a power of 2');
end
endfunction
