#include <Adafruit_NeoPixel.h>


#define PIN            3 //pixel pin
#define BUTTON_PIN   7 // button pin
#define NUMPIXELS      16

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

int delayval = 100; // delay for half a second
bool oldState = HIGH;
int showType = 0;

void setup() {

  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pixels.begin(); // This initializes the NeoPixel library.
}

void loop() {
  //bool newState = digitalRead(BUTTON_PIN);
 // if (newState == LOW && oldState == HIGH) {
    // Short delay to debounce button.
    delay(20);
    // Check if button is still low after debounce.
 //   newState = digitalRead(BUTTON_PIN);
//    if (newState == LOW) {
      showType++;
      if (showType > 9)
        showType=0;
      startShow(showType);
//    }
 // }

 
  delay(500); 
 // oldState = newState;
}
void startShow(int i) {
  switch(i){
    case 0: colourWipe(pixels.Color(0, 0, 0), 50);    // Black/off
            break;
    case 1: colourOpposite(255,0,0,0,255,0);  // Red/green
            break;
    case 2: colourRotate(255,0,0);  // Red
            break;
    case 3: colourWipe(pixels.Color(0, 0, 255), 50);  // Blue
            break;
    case 4: colourOpposite(0,255,0,0,0,255); // green/blue
            break;
    case 5: colourWipe(pixels.Color(127,127,0), 50); //yellow
            break;
    case 6: colourRotate(255,255,255);
            break;
    case 7: 
            break;
    case 8: 
            break;
    case 9:             break;
  }
}
void colourWipe(uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i<pixels.numPixels(); i++) {
    pixels.setPixelColor(i, c);
    pixels.show();
    delay(wait);
  }
}
void colourRotate(int r, int g, int b) {
  for(uint16_t i=0; i<pixels.numPixels(); i++) {
    pixels.setPixelColor(i, pixels.Color(0,0,0));
    pixels.show();
  }
  for(int i=0;i<NUMPIXELS;i++){

    // pixels.Color takes RGB values, from 0,0,0 up to 255,255,255
    pixels.setPixelColor(i, pixels.Color(r,g,b)); // Moderately bright green color.

    pixels.show(); // This sends the updated pixel color to the hardware.
    delay(500);
    pixels.setPixelColor(i, pixels.Color(0,0,0));

  }
}
void colourOpposite(int r, int g, int b, int r2, int g2, int b2) {
  for(uint16_t i=0; i<pixels.numPixels(); i++) {
    pixels.setPixelColor(i, pixels.Color(0,0,0));
    pixels.show();
  }
  int j=NUMPIXELS/2;
  for(int i=0;i<NUMPIXELS;i++){

    // pixels.Color takes RGB values, from 0,0,0 up to 255,255,255
    pixels.setPixelColor(i, pixels.Color(r,g,b)); // Moderately bright green color.
    pixels.setPixelColor(j, pixels.Color(r2,g2,b2)); // Moderately bright green color.

    pixels.show(); // This sends the updated pixel color to the hardware.
    delay(500);
    pixels.setPixelColor(i, pixels.Color(0,0,0));
    pixels.setPixelColor(j, pixels.Color(0,0,0));
    j++;
    if (j>=NUMPIXELS) {
      j=0;
    }
   }
}
