void setup()
{
    pinMode(13, OUTPUT);
    pinMode(7, INPUT);
}

void loop()
{
    int val = digitalRead(7)
    digitalWrite(13, val)
}