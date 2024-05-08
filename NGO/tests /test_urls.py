from django.test import TestCase
from django.urls import reverse,resolve
from NGO.views import *
class TestUrls(TestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func,home)
    
    def test_admin_login_url_is_resolved(self):
        url = reverse('login_admin')
        self.assertEqual(resolve(url).func,adminlogin)
    
    def test_donor_login_url_is_resolved(self):
        url = reverse('login_donor')
        self.assertEqual(resolve(url).func,donorlogin)

    def test_register_donor_login_url_is_resolved(self):
        url = reverse('register_donor')
        self.assertEqual(resolve(url).func,donorRegistration)
    
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func,logout)
    
    def test_viewDonor_url_is_resolved(self):
        url = reverse('viewDonor')
        self.assertEqual(resolve(url).func,donorview)
    
    def test_pledgehist_url_is_resolved(self):
        url = reverse('pledgehist')
        self.assertEqual(resolve(url).func,pledgeh)
    
    def test_studentdetails_url_is_resolved(self):
        url = reverse('studentdetails')
        self.assertEqual(resolve(url).func,studentdetails)
    
    def test_delete_student_url_is_resolved(self):
        url = reverse('delete_student',args=[0])
        self.assertEqual(resolve(url).func,deletestudent)
    
    def test_modify_student_url_is_resolved(self):
        url = reverse('modify_student',args=[0])
        self.assertEqual(resolve(url).func,modifystudent)
    
    def test_edit_estimation_table_url_is_resolved(self):
        url = reverse('editesttbl')
        self.assertEqual(resolve(url).func,editest)
    
    def test_working_status_url_is_resolved(self):
        url = reverse('workingstats')
        self.assertEqual(resolve(url).func,vstats)
    
    def test_maintain_inventory_url_is_resolved(self):
        url = reverse('maintaininv')
        self.assertEqual(resolve(url).func,minventory)
    
    def test_show_donor_url_is_resolved(self):
        url = reverse('show-donor',args=[0])
        self.assertEqual(resolve(url).func,viewdonor)
    
    def test_click_paid_url_is_resolved(self):
        url = reverse('click-paid',args=[0])
        self.assertEqual(resolve(url).func,clickp)
    
    def test_update_row_url_is_resolved(self):
        url = reverse('update-row',args=[1])
        self.assertEqual(resolve(url).func,changeestimate)
    
    def test_update_inv_url_is_resolved(self):
        url = reverse('update-inv',args=[1])
        self.assertEqual(resolve(url).func,inven)
    
    def test_exph_url_is_resolved(self):
        url = reverse('vexp')
        self.assertEqual(resolve(url).func,exph)
    
    def test_aexpend_url_is_resolved(self):
        url = reverse('aexpend')
        self.assertEqual(resolve(url).func,updatetexp)



































