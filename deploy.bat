@echo off
echo.
echo ==========================================
echo    AVILA TRANSPORTES - DEPLOY SCRIPT
echo ==========================================
echo.

cd /d "c:\Users\NicolasAvila\Desktop\Avila DevOps\ordem de coleta"

echo [1/6] Inicializando repositorio Git...
git init
echo.

echo [2/6] Adicionando arquivos...
git add .
echo.

echo [3/6] Fazendo commit inicial...
git commit -m "Initial commit - Avila Transportes System v2.0"
echo.

echo [4/6] Configurando branch main...
git branch -M main
echo.

echo [5/6] Conectando ao GitHub...
echo Digite o comando abaixo no terminal:
echo git remote add origin https://github.com/avilatransportes/sistema-coleta.git
echo.

echo [6/6] Para fazer push:
echo git push -u origin main
echo.

echo ==========================================
echo    PROXIMOS PASSOS:
echo ==========================================
echo 1. Crie o repositorio no GitHub: 
echo    https://github.com/new
echo    Nome: sistema-coleta
echo    Owner: avilatransportes
echo.
echo 2. Execute: git remote add origin [URL_DO_REPO]
echo.
echo 3. Execute: git push -u origin main
echo.
echo 4. Deploy no Streamlit Cloud:
echo    https://share.streamlit.io
echo.
echo 5. Configure DNS do dominio
echo ==========================================

pause
