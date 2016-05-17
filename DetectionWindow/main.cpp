#include <QtGui/QApplication>
#include "detectionwindow.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    DetectionWindow w;
    w.show();
    
    return a.exec();
}
