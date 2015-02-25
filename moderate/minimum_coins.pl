#!/usr/bin/env perl
# CodeEval - Minimum Coins
# https://www.codeeval.com/open_challenges/74/

use strict;

my @coins = (5, 3, 1);

sub calc_numb_coins {
    my @coins_to_return = ();
    my $amount = shift @_;
    
    foreach my $coin (@coins){
        my $quotient = $amount / $coin;
        if ($quotient >= 1){
            my $number_of_coins = sprintf("%d", $quotient);
            for (my $i = 0; $i < $number_of_coins; $i++){
                #print "coin: $coin ";
                push(@coins_to_return, $coin);
            }
            $amount -= $number_of_coins * $coin;                
        }

        if (!$amount){
            return @coins_to_return;
        }
    }
}

open(INFILE, "<", $ARGV[0]) or die("Cannot open file $ARGV[0] for reading: $!");
while(my $line = <INFILE>) {
    next if($line =~ m/^\s$/);  
    $line =~ s/(^\s|\s*$)//g;   
    my $amount = $line;
    my @number_of_coins = calc_numb_coins($amount);
    print scalar @number_of_coins;
    print "\n";
}
close(INFILE);
