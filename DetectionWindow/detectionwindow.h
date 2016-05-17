#ifndef DETECTIONWINDOW_H
#define DETECTIONWINDOW_H

#include <QWidget>

namespace Ui {
class DetectionWindow;
}

class DetectionWindow : public QWidget
{
    Q_OBJECT
    
public:
    explicit DetectionWindow(QWidget *parent = 0);
    ~DetectionWindow();
    
private:
    Ui::DetectionWindow *ui;
};

#endif // DETECTIONWINDOW_H
