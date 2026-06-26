export const metadata = {
  title: "H.B-SYST",
  description: "Ask H.B-SYST",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="fa" dir="rtl">
      <body style={{ margin: 0, fontFamily: "sans-serif", background: "#fafafa" }}>
        {children}
      </body>
    </html>
  );
}
