// Click-to-zoom for mermaid diagrams
document.addEventListener('DOMContentLoaded', function() {
    // Create overlay
    const overlay = document.createElement('div');
    overlay.className = 'mermaid-zoom-overlay';
    document.body.appendChild(overlay);

    // Close on click
    overlay.addEventListener('click', function() {
        overlay.classList.remove('active');
        overlay.innerHTML = '';
    });

    // Close on Escape
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && overlay.classList.contains('active')) {
            overlay.classList.remove('active');
            overlay.innerHTML = '';
        }
    });

    // Add click handlers to all mermaid diagrams
    document.querySelectorAll('pre.mermaid').forEach(function(mermaid) {
        mermaid.style.cursor = 'zoom-in';
        mermaid.addEventListener('click', function() {
            const svg = mermaid.querySelector('svg');
            if (svg) {
                const clone = svg.cloneNode(true);
                overlay.innerHTML = '';
                overlay.appendChild(clone);
                overlay.classList.add('active');
            }
        });
    });
});
