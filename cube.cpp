#include <bits/stdc++.h>
using namespace std;

/*random input - wwwwwwwwwyyyyyyyyybbbbbbbbbgggggggggooooooooorrrrrrrrr*/

/* facing the white at orgin  y|  /z
 * 	MY ASSUMPTION OF THE 	   | /
 *  CUBE IN 3D                 |/______ x
 *                             o
 */
 
class Point{
	public:
	  int x,y,z;
	  static int xval,yval,zval;
	  Point(){
		  /* xval,yval,zval are the co-ordinates of a side of a piece, we have to 
		   * update them so that each piece can take the exact count of sides as input
		   * PENDING WORK
		   */
		  x = ((xval+(yval/3)))%3;
		  y = (yval)%3;
		  z = (zval-(yval/9));
		  yval = yval + 1;
		  //cout << x << " " << y << " " << z << endl;
	  }
};
int Point::xval=0,Point::yval=0,Point::zval=0;

class Side{
	/* Each side is associated with a color and the co-ordinate of the piece in the
	 * x-y-z axis
	 */
	public:
	  char C;
	  Point P;
	  Side(){
		  //cout << "Enter color: ";
		  cin >> C;
	  }
	  Side(Side *other) {
        P.x = other->P.x;
        P.y = other->P.y;
        P.z = other->P.z;
        C = other->C;
    }
};

class Piece{
	/* Each piece can have upto 3 sides or may be 2 or 1, hence updating dynamically
	 * based on co-ordinates we have to take the number of sides as input
	 * Currently have to fix this
	 */
	public:
	  Side *S[3];
	  Piece *next=NULL;
	  Piece(bool n){
		  for(int i =0;i<3-int(n);i++){
			  S[i]=new Side;
		  }
		  if (int(n))S[2]=NULL;
	  }
	  Piece(Piece *temp){
		  for (int i =0;i<3;i++){
		     S[i] = temp->S[i];
	      }
		  next = temp->next;
	  }
};

class Cube{
	/* Creating a 3d linked list to represent each piece
	 * 
	 * For now i just created class with a linear linkedlist and i have to make it
	 * 3d linked list
	 */
	static int count;
	Piece *piece=NULL;
	public:
	  void add_piece(){
		  Piece *p = new Piece(bool((Point::xval%2==0)&&(Point::yval%2==0)));
		  if (piece==NULL){
			  piece = p;
		  }
		  else{
			  Piece *temp = piece;
			  while(temp->next!=NULL){
				  temp = temp->next;
			  }
			  temp->next = p;
		  }
		  //cout << count++ << endl;
	  }
	  void print_cube(){
		  Piece *temp = piece;
		  while(temp!=NULL){
			  int i = 0;
			  while(temp->S[i]!=NULL){
				  cout << temp->S[i++]->C << " ";
			  }
			  temp = temp->next;
		  }
	  }
	  /*just rotating the linked lists is enough for the cube rotations with adjusting
	   * the links to other nodes
	   */
	  void R(){
	  }
	  void L(){
	  }
	  void U(){
	  }
	  void D(){
	  }
	  void F(){
	  }
};

int Cube::count=1;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie();
    Cube c;
    /* Actually there are 26 pieces but due to the xval yval issue i have to
     * use 27 pieces,some error:)
     */
    for(int i = 0;i<=26;i++){
		c.add_piece();
	}
	cout << " All piece noted"<<endl;
	c.print_cube();
    return 0;
}
