{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Write a while loop that lets the user enter a number.\n",
    "#The number should be multiplied by 10, and the result assigned to a variable named product. \n",
    "#The loop should iterate as long as product is less than 100. \n",
    "\n",
    "product=0\n",
    "while product < 100: \n",
    "    number = float(input('Enter a number:')) \n",
    "    product = number * 10 \n",
    "    print('product = ', product)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Find the total hours worked.\n"
     ]
    }
   ],
   "source": [
    "#2. Write a while loop that asks the user to enter two numbers.\n",
    "#The numbers should be added and the sum displayed.\n",
    "#The loop should ask the user if he or she wishes to perform the operation again. \n",
    "#If so, the loop should repeat, otherwise it should terminate.\n",
    "working_days=0\n",
    "weekend = 'y'\n",
    "\n",
    "print('Find the total hours worked.')\n",
    "\n",
    "while weekend =='N':\n",
    "    monday= int(input('Enter total hours worked on monday: '))\n",
    "    tuesday=int(input('Enter total hours worked tuesday: '))\n",
    "    Hours_worked= monday + tuesday\n",
    "    print('For both days, the total hours worked:',Hours_worked)\n",
    "    weekend=input('Calculate another Hours worked? Enter y for yes): ')\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Find the total calories consumed for breakfast and dinner.\n"
     ]
    }
   ],
   "source": [
    "calories=0\n",
    "another = 'y'\n",
    "\n",
    "print('Find the total calories consumed for breakfast and dinner.')\n",
    "\n",
    "while another =='y':\n",
    "    breakfast= int(input('Enter total calories consumed for breakfast: '))\n",
    "    dinner=int(input('Enter total calories consumed for dinner: '))\n",
    "    calories= breakfast + dinner\n",
    "    print('For both meals, the total calories consumed:',calories)\n",
    "    another=input('Calculate another set of calories? Enter y for yes): ')\n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#2. Write a while loop that asks the user to enter two numbers.\n",
    "#The numbers should be added and the sum displayed.\n",
    "#The loop should ask the user if he or she wishes to perform the operation again. \n",
    "#If so, the loop should repeat, otherwise it should terminate.\n",
    "working_days=0\n",
    "weekend = 'y'\n",
    "\n",
    "print('Find the total hours worked.')\n",
    "\n",
    "while weekend =='N':\n",
    "    monday= int(input('Enter total hours worked on monday: '))\n",
    "    tuesday=int(input('Enter total hours worked tuesday: '))\n",
    "    Hours_worked= monday + tuesday\n",
    "    print('For both days, the total hours worked:',Hours_worked)\n",
    "    weekend=input('Calculate another Hours worked? Enter y for yes): ')\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
