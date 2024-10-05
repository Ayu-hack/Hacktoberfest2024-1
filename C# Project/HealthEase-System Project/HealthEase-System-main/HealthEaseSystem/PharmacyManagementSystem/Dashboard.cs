using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


namespace PharmacyManagementSystem
{
    public partial class Dashboard : Form
    {
        private Color endBackColor = Color.OliveDrab;
        private Color startForeColor = Color.White;
        private Color previousBackColor= Color.SlateBlue;
     
        public Dashboard()
        {
            InitializeComponent();
            CountMed();
            CountSellers();
            CountCustomer();
            SumAmt();
            GetSeller();
            GetBestSeller();
            GetBestCustomer();
        }
        SqlConnection conn = new SqlConnection(@"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\syedm\OneDrive\Documents\PharmacySystemDB.mdf;Integrated Security=True;Connect Timeout=30");

        private void CountMed()
        {
            conn.Open();
            SqlDataAdapter sda = new SqlDataAdapter("Select Count(*) from MedicineTbl", conn);
            DataTable dt = new DataTable();
            sda.Fill(dt);
            MedicineNum.Text = dt.Rows[0][0].ToString();
            conn.Close();
        }

        private void CountSellers()
        {
            conn.Open();
            SqlDataAdapter sda = new SqlDataAdapter("Select Count(*) from SellerTbl", conn);
            DataTable dt = new DataTable();
            sda.Fill(dt);
            SellerLbl.Text = dt.Rows[0][0].ToString();
            conn.Close();
        }

        private void CountCustomer()
        {
            conn.Open();
            SqlDataAdapter sda = new SqlDataAdapter("Select Count(*) from CustomerTbl", conn);
            DataTable dt = new DataTable();
            sda.Fill(dt);
            CustomerLbl.Text = dt.Rows[0][0].ToString();
            conn.Close();
        }
        private void SumAmt()
        {
            conn.Open();
            SqlDataAdapter sda = new SqlDataAdapter("Select Sum(BillAmount) from BillTbl", conn);
            DataTable dt = new DataTable();
            sda.Fill(dt);
            SellAmtLbl.Text = "RS " + dt.Rows[0][0].ToString();
            conn.Close();
        }
        private void SumAmtBySeller()
        {
            conn.Open();
            SqlDataAdapter sda = new SqlDataAdapter("Select Sum(BillAmount) from BillTbl where SellerName='" + SellerCb.SelectedValue.ToString() + "'", conn);
            DataTable dt = new DataTable();
            sda.Fill(dt);
            SellsBySellerLbl.Text = "RS " + dt.Rows[0][0].ToString();
            conn.Close();
        }
        private void GetSeller()
        {
            conn.Open();
            SqlCommand cmd = new SqlCommand("Select SellerName from SellerTbl ", conn);
            SqlDataReader Rdr;
            Rdr = cmd.ExecuteReader();
            DataTable dt = new DataTable();
            dt.Columns.Add("SellerName", typeof(string));
            dt.Load(Rdr);
            SellerCb.ValueMember = "SellerName";
            SellerCb.DataSource = dt;

            conn.Close();
        }
        private void GetBestSeller()
        {
            try
            {
                conn.Open();
                string Innerquery = "Select Max(BillAmount) from BillTbl";
                DataTable dt1 = new DataTable();
                SqlDataAdapter sda1 = new SqlDataAdapter(Innerquery, conn);
                sda1.Fill(dt1);
                string query = "Select SellerName from BillTbl where BillAmount = '" + dt1.Rows[0][0].ToString() + "'";
                SqlDataAdapter sda = new SqlDataAdapter(query, conn);
                DataTable dt = new DataTable();
                sda.Fill(dt);
                BestSellerLbl.Text = dt.Rows[0][0].ToString();
                conn.Close();

            }
            catch (Exception Ex)
            {
                Console.WriteLine("Exception occurred: " + Ex.Message);

                conn.Close();
            }
        }

        private void GetBestCustomer()
        {
            try
            {
                conn.Open();
                string Innerquery = "Select Max(BillAmount) from BillTbl";
                DataTable dt1 = new DataTable();
                SqlDataAdapter sda1 = new SqlDataAdapter(Innerquery, conn);
                sda1.Fill(dt1);
                string query = "Select CustomerName from BillTbl where BillAmount = '" + dt1.Rows[0][0].ToString() + "'";
                SqlDataAdapter sda = new SqlDataAdapter(query, conn);
                DataTable dt = new DataTable();
                sda.Fill(dt);
                BestCustomerLbl.Text = dt.Rows[0][0].ToString();
                conn.Close();

            }
            catch (Exception Ex)
            {
                Console.WriteLine("Exception occurred: " + Ex.Message);

                conn.Close();
            }
        }
        private void pictureBox14_Click(object sender, EventArgs e)
        {

        }

        private void label20_Click(object sender, EventArgs e)
        {
            Login loginForm = new Login();
            loginForm.Show();
            this.Close();
        }

        private void SellerCb_SelectionChangeCommitted(object sender, EventArgs e)
        {
            SumAmtBySeller();
        }

        private void BestSellerLbl_Click(object sender, EventArgs e)
        {

        }

        private void label18_Click(object sender, EventArgs e)
        {
            Manufacturer obj = new Manufacturer();
            obj.Show();
            this.Hide();
        }

        private void label16_Click(object sender, EventArgs e)
        {
            Medicines medicines = new Medicines();
            medicines.Show();
            this.Hide();
        }

        private void label17_Click(object sender, EventArgs e)
        {
            Customer obj = new Customer();
            obj.Show();
            this.Hide();
        }

        private void label19_Click(object sender, EventArgs e)
        {
            Sellers obj = new Sellers();
            obj.Show();
            this.Hide();
        }

        private void label15_Click(object sender, EventArgs e)
        {

        }

        private void panel11_MouseHover(object sender, EventArgs e)
        {
            panel11.BackColor = endBackColor;
            panel11.ForeColor = startForeColor;
        }

        private void panel11_MouseLeave(object sender, EventArgs e)
        {
            panel11.BackColor = previousBackColor; 
            
        }

        private void panel2_Paint(object sender, PaintEventArgs e)
        {

        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void panel11_Paint(object sender, PaintEventArgs e)
        {
            Panel panel = (Panel)sender;

            int borderWidth = 6; // Adjust the width of the border as needed
            int cornerRadius = 13; // Adjust the corner radius as needed

            using (Graphics g = e.Graphics)
            using (Pen borderPen = new Pen(Color.Indigo, borderWidth))
            using (GraphicsPath path = new GraphicsPath())
            {
                // Create a rounded rectangle path
                path.AddArc(panel.ClientRectangle.X, panel.ClientRectangle.Y, cornerRadius * 2, cornerRadius * 2, 180, 90);
                path.AddArc(panel.ClientRectangle.Width - (cornerRadius * 2), panel.ClientRectangle.Y, cornerRadius * 2, cornerRadius * 2, 270, 90);
                path.AddArc(panel.ClientRectangle.Width - (cornerRadius * 2), panel.ClientRectangle.Height - (cornerRadius * 2), cornerRadius * 2, cornerRadius * 2, 0, 90);
                path.AddArc(panel.ClientRectangle.X, panel.ClientRectangle.Height - (cornerRadius * 2), cornerRadius * 2, cornerRadius * 2, 90, 90);
                path.CloseFigure();

                // Draw the rounded border
                g.DrawPath(borderPen, path);
            }
        }

        private void Dashboard_Load(object sender, EventArgs e)
        {

        }
    }
}
