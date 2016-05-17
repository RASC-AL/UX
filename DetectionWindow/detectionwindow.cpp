#include "detectionwindow.h"
#include "ui_detectionwindow.h"

DetectionWindow::DetectionWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::DetectionWindow)
{
    ui->setupUi(this);
}

DetectionWindow::~DetectionWindow()
{
    delete ui;
}
