#!/usr/bin/env perl
# CodeEval - Card Number Validation
# https://www.codeeval.com/open_challenges/172/

use strict;

sub check_number {
    my $number_str = shift @_;
    $number_str = reverse $number_str;
    my @number_str_arr = split //, $number_str;
    my $arr_length = @number_str_arr;
    my $sum = 0;
    my $i = 0;
    while ($i < $arr_length){
        if ($i %2){
            my $prod = $number_str_arr[$i] * 2;
            if ($prod > 9){
                my $sum_of_digits = 0;
                my @prod_arr = split //, $prod;
                foreach my $digit (@prod_arr){
                    $sum_of_digits += $digit;
                }
                $sum += $sum_of_digits;
            }
            else {
                $sum += $number_str_arr[$i] * 2;
            }
        }
        else {
            $sum += $number_str_arr[$i];
        }
        $i++;
    }

    if ($sum % 10){
        return 0;
    }
    else {
        return 1;
    }
}

open(INFILE, "<", $ARGV[0]) or die("Cannot open file $ARGV[0] for reading: $!");
while(my $number = <INFILE>) {
    next if($number =~ m/^\s$/);  
    $number =~ s/\s//gc;
    print check_number($number), "\n";
}
