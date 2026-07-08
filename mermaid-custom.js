// Custom mermaid enhancements - runs AFTER preprocessor's mermaid-init.js
document.addEventListener('DOMContentLoaded', function() {
    // Wait for preprocessor to finish, then add our enhancements
    setTimeout(function() {
        // Add zoom functionality to all mermaid diagrams
        document.querySelectorAll('pre.mermaid').forEach(function(mermaid) {
            // Skip if already has zoom handler
            if (mermaid.dataset.zoomAdded) return;
            mermaid.dataset.zoomAdded = 'true';

            mermaid.style.cursor = 'zoom-in';
            mermaid.addEventListener('click', function() {
                var svg = mermaid.querySelector('svg');
                if (svg) {
                    var overlay = document.querySelector('.mermaid-zoom-overlay');
                    if (!overlay) {
                        overlay = document.createElement('div');
                        overlay.className = 'mermaid-zoom-overlay';
                        document.body.appendChild(overlay);
                        overlay.addEventListener('click', function() {
                            overlay.classList.remove('active');
                            overlay.innerHTML = '';
                        });
                        document.addEventListener('keydown', function(e) {
                            if (e.key === 'Escape' && overlay.classList.contains('active')) {
                                overlay.classList.remove('active');
                                overlay.innerHTML = '';
                            }
                        });
                    }
                    var clone = svg.cloneNode(true);
                    overlay.innerHTML = '';
                    overlay.appendChild(clone);
                    overlay.classList.add('active');
                }
            });
        });
    }, 500);
});
