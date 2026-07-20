#include <SFML/Graphics.hpp>
#include <time.h>
using namespace sf;

int main()
{
    srand(time(0));

    RenderWindow app(VideoMode(400, 400), "Minesweeper!");

    int w=32;
    int grid[12][12];
    int sgrid[12][12]; //for showing

    Texture t;
    t.loadFromFile("images/tiles.jpg");
    Sprite s(t);

    for (int i=1;i<=10;i++)
     for (int j=1;j<=10;j++)
      {
        sgrid[i][j]=10;
        if (rand()%5==0)  grid[i][j]=9;
        else grid[i][j]=0;
      }

    for (int i=1;i<=10;i++)
     for (int j=1;j<=10;j++)
      {
        int n=0;
        if (grid[i][j]==9) continue;
        if (grid[i+1][j]==9) n++;
        if (grid[i][j+1]==9) n++;
        if (grid[i-1][j]==9) n++;
        if (grid[i][j-1]==9) n++;
        if (grid[i+1][j+1]==9) n++;
        if (grid[i-1][j-1]==9) n++;
        if (grid[i-1][j+1]==9) n++;
        if (grid[i+1][j-1]==9) n++;
        grid[i][j]=n;
      }

    while (app.isOpen())
    {
        Vector2i pos = Mouse::getPosition(app);
        int x = pos.x/w;
        int y = pos.y/w;

        Event e;
        while (app.pollEvent(e))
        {
            if (e.type == Event::Closed)
                app.close();

            if (e.type == Event::MouseButtonPressed)
              if (e.key.code == Mouse::Left) sgrid[x][y]=grid[x][y];
              else if (e.key.code == Mouse::Right) sgrid[x][y]=11;
        }

        app.clear(Color::White);

        for (int i=1;i<=10;i++)
         for (int j=1;j<=10;j++)
          {
           if (sgrid[x][y]==9) sgrid[i][j]=grid[i][j];
           s.setTextureRect(IntRect(sgrid[i][j]*w,0,w,w));
           s.setPosition(i*w, j*w);
           app.draw(s);
          }

        app.display();
    }

    return 0;
}
