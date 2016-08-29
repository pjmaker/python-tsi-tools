CSV=Alice-2015.csv AliceSolar-2015.csv Darwin-2015.csv DarwinSolar-2015.csv

all: $(CSV)

Alice-2015.csv:
	grep ,2015, < HM01X_Data_015590_999999999248202.txt > $@

Darwin-2015.csv:
	grep ,2015, < HM01X_Data_014015_999999999248202.txt > $@

AliceSolar-2015.csv:
	awk -f make-solar.awk < DC02D_Data_015590_999999999248204.txt > tmp
	sed 's/,  *$/, NaN//' < tmp > $@

DarwinSolar-2015.csv:
	awk -f make-solar.awk < DC02D_Data_014015_999999999248204.txt > tmp
	sed 's/,  *$/, NaN//' < tmp > $@

clean:
	-rm $(CSV)
